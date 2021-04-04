"""Base model."""

# Django
from django.db import models


class BaseModel(models.Model):
    """Base Model class."""

    created = models.DateTimeField(
        verbose_name='creado en',
        auto_now_add=True,
        help_text='Fecha y hora en la que se creó el objeto.',
    )
    modified = models.DateTimeField(
        verbose_name='modificado en',
        auto_now=True,
        help_text='Fecha y hora en la que se modificó por última vez el objeto.',
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ('-created', '-modified')
