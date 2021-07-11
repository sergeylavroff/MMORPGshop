from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reply, UserNotif
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=Reply)
def notify_of_reply(sender, instance, created, **kwargs):
    if created:
        subject = f'Пользователь {instance.user} откликнулся на ваше объявление {instance.article}'
        message = f'Текст сообщения {instance.text}'
        author = instance.article.author.email
        send_mail(subject, message, from_email=None, recipient_list=[author])
    else:
        user_email = instance.user.email
        subject = f'Отклик принят'
        message = f'{instance.user} автор объявления {instance.article} принял Ваш отклик.'
        send_mail(subject, message, from_email=None, recipient_list=[user_email])

@receiver(post_save, sender=UserNotif)
def notify_of_news(sender, instance, **kwargs):
    users = User.objects.all()
    for user in users:
        msg = EmailMultiAlternatives(
            instance.name,
            body=None,
            from_email=None,
            to=[user.email],
        )
        msg.attach_alternative(instance.body, "text/html")
        msg.send()
