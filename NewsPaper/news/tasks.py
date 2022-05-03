from celery import shared_task
import time
from .management.commands.runapscheduler import *

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post


@shared_task
def send_email_new_post(datapk, mail, name):
    data = Post.objects.get(pk=datapk)
    html_content = render_to_string(
        'new_post_email.html', {
            "data": data, "recipient": name, }
    )
    email_i = [mail]
    msg = EmailMultiAlternatives(
        subject=f'Новый пост: {data.post_title}',
        body=data.post_text,
        from_email='django_test123@sobago.ru',
        to=email_i,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_weekly_news():
    weekly_news_subscribers()
