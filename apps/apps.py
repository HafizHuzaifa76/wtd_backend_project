"""
Django App Configuration
"""
from django.apps import AppConfig


class AppsConfig(AppConfig):
    """
    Configuration for the apps application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    verbose_name = 'Apps'

