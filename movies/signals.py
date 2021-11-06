from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie
from django.core.mail import send_mail


@receiver(post_save, sender=Movie)
def my_handler(sender, instance, created, *args, **kwargs):
    print("signal is working fine")
    # send_mail('New Movie Created', f'Dear User {instance.name}',
    #           'moaazmoustafa@gmail.com', ['moaazmoustafa@outlook.com'], fail_silently=False)
