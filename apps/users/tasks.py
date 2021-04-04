"""User tasks."""

# Celery
from os import name

from config import celery_app

# Python
from datetime import timedelta

# PyJWT
import jwt

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

# Django REST framework
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from apps.users.models import User


def generate_verification_token(user) -> str:
    exp_date = timezone.now() + timedelta(hours=1)
    payload = {
        'user': user.email,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token: str = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


@celery_app.task()
def send_confirmation_email(user_pk):
    user = User.objects.get(pk=user_pk)
    verification_token = generate_verification_token(user)
    subject, from_email, to = 'hello_talana', 'enrique.costam@gmail.com', [user.email]
    text_content = render_to_string(
        'account/email_confirm.html', {
            'token': verification_token,
            'user': user
        }
    )
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(text_content, "text/html")
    msg.send()
