"""
Django Admin Configuration
Register your models here to manage them via Django admin panel.
"""
from django.contrib import admin
from apps.models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    """
    Admin configuration for Example model.
    """
    list_display = ('id', 'name', 'description', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)

