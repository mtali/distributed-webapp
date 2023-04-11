from django.contrib import admin

from hubs.models import Hub


@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id', 'country', 'region', 'created_at', 'updated_at')
    list_filter = ('country', 'region')
    search_fields = ('name', 'device_id', 'country', 'region')
