import logging
import datetime

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from ...models import Category, Post

logger = logging.getLogger(__name__)


def weekly_news_subscribers():
    categorys = Category.objects.all()
    new_posts = {}
    cat_users = {}
    emails_users = {}
    for cat in categorys:
        users_for_cat = []
        for user in cat.subscribers.all():
            if user.email != '':
                emails_users[user] = user.email
                users_for_cat.append(user.username)

            else:
                continue
        for user in emails_users:
            cat_users[user.username] = [cat.cat_name for cat in Category.objects.filter(subscribers=user)]
        start_date = datetime.date.today() - datetime.timedelta(weeks=1)
        end_date = datetime.date.today()
        if Post.objects.filter(post_to_category_rel=cat, create_date_time__range=(start_date, end_date)):
            new_posts[cat.cat_name] = Post.objects.filter(post_to_category_rel=cat, create_date_time__range=(start_date, end_date))

    def get_news_for_user(user, cat, new_posts):
        data = {}
        for i in cat:
            data[i] = new_posts[i]
        send_mail_weekly(user.email, user.username, data)

    for user in emails_users:
        get_news_for_user(user, cat_users[user.username], new_posts)


def send_mail_weekly(email, user, category_posts):
    html_content = render_to_string(
        'new_posts_weekly_email.html', {
            "data": category_posts, "recipient": user, }
    )
    body_text = ''
    for cat in category_posts:
        body_text += f'Категория: {cat}\n'
        for post in category_posts[cat]:
            body_text += f'{post.post_title}\n'
            body_text += f'{post.post_text}\n\n'
    msg = EmailMultiAlternatives(
        subject=f'Привет, {user}! Новые посты за неделю!',
        body=body_text,
        from_email='django_test123@sobago.ru',
        to=[email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            weekly_news_subscribers,
            trigger=CronTrigger(day_of_week="mon", hour="09", minute="00"),
            id="weekly_news_subscribers",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
