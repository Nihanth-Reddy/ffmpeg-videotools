from django.core.mail import EmailMessage
from django.conf import settings


def send_email(email):
    email_subject = 'Thank you for your review'
    email_body = "Your video has been successfully processed"

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)