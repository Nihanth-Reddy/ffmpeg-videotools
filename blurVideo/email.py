from django.core.mail import EmailMessage
from django.conf import settings


def send_email(email):
    email_subject = 'Video Processing has been completed'
    email_body = "Your video has been successfully blurred"

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)