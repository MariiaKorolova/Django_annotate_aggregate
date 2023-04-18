from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send(email, text_celery_ex):
    send_mail(
        'This my new program',
        text_celery_ex,
        'masha.korolyova17@gmail.com',
        [email, ],
        fail_silently=False,
    )