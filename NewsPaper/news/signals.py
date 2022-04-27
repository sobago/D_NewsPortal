from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post, Category


def email_new_post(data):
    recipients = []
    category = data.post_to_category_rel
    for i in category.subscribers.all():
        if i.email == "":
            continue
        else:
            recipients.append([i.email, i.username])
    for i, j in recipients:
        html_content = render_to_string(
            'new_post_email.html', {
                "data": data, "recipient": j, }
        )
        email_i = [i]
        msg = EmailMultiAlternatives(
            subject=f'Новый пост: {data.post_title}',
            body=data.post_text,
            from_email='django_test123@sobago.ru',
            to=email_i,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, **kwargs):
    email_new_post(instance)
