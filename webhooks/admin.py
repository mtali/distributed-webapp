from django.contrib import admin

from webhooks.models import Webhook


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'processed', 'type')
    list_display = ('id', 'processed', 'type', 'timestamp', 'created_at')
