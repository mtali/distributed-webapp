import uuid

from django.db import models


class Webhook(models.Model):
    WEBHOOK_TYPE_CHOICES = (
        ('SwapSale', 'SwapSale'),
        ('NewUser', 'NewUser'),
        ('UpdateUser', 'UpdateUser'),
        ('MembershipSale', 'MembershipSale'),
        ('PackUpdate', 'PackUpdate')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100, choices=WEBHOOK_TYPE_CHOICES)
    payload = models.JSONField()
    timestamp = models.DateTimeField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'webhooks'
