from django.contrib import admin

from .models import Pack


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ['pack_id', 'pack_status', 'current_customer', 'is_active', 'created_at', 'updated_at']
    search_fields = ['pack_id']
    list_filter = ['created_at', 'updated_at', 'pack_status', 'is_active']
