"""User admin."""

# Django
from django.contrib import admin

# Models
from .models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin class."""

    list_display = ('id', 'email')
    list_display_links = ('id', 'email')

    fieldsets = (
        ('Personal information', {
            'fields': (
                'email', 'password', 'first_name', 'last_name', 'is_verified'
            )
        }),
        ('Privileges', {
            'fields': (
                'is_active',  'is_staff', 'is_superuser',
            )
        }),
        ('Permissions', {
            'fields': (
                'groups', 'user_permissions'
            )
        }),
        ('Date and time information', {
            'fields': (
                'last_login', 'date_joined'
            )
        }),
        ('Metadata', {
            'fields': (
                'created', 'modified'
            )
        }),
    )

    readonly_fields = ('created', 'modified')

