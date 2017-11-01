from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail


def email(request):
    email_subject = 'Email test'
    email_message = 'This is a test.'
    email_from = getattr(settings, 'EMAIL_HOST_USER', '')
    email_to = ['jfer.garciav@gmail.com']

    send_mail(email_subject, email_message, email_from, email_to, fail_silently=False)

    return HttpResponse('Email sent')
