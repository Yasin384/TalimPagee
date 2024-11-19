from django.core.mail import send_mail
from django.conf import settings

def send_notification_email(subject, message, recipient_list):
    """
    Utility function to send notification emails.
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )
