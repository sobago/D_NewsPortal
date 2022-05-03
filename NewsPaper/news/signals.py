from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from allauth.account.signals import user_signed_up
from .tasks import send_email_new_post

from .models import Post


def email_new_post(data):
    recipients = []
    category = data.post_to_category_rel
    for i in category.subscribers.all():
        if i.email == "":
            continue
        else:
            recipients.append([i.email, i.username])
    for mail, name in recipients:
        send_email_new_post.apply_async([data.pk, mail, name], countdown=5)
        # html_content = render_to_string(
        #     'new_post_email.html', {
        #         "data": data, "recipient": name, }
        # )
        # email_i = [mail]
        # msg = EmailMultiAlternatives(
        #     subject=f'Новый пост: {data.post_title}',
        #     body=data.post_text,
        #     from_email='django_test123@sobago.ru',
        #     to=email_i,
        # )
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()


@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, **kwargs):
    email_new_post(instance)


@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def greet_new_user(request, user, **kwargs):
    html_content = render_to_string(
        'new_user_greet_email.html', {
            "user": user, }
    )
    msg = EmailMultiAlternatives(
        subject=f'Добро пожаловать!',
        body=f'Приветствуем тебя, {user.username} на нашем портале',
        from_email='django_test123@sobago.ru',
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
