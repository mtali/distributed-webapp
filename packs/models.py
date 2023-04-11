from django.core.validators import RegexValidator
from django.db import models

from customers.models import Customer
from hubs.models import Hub


class Pack(models.Model):
    PACK_STATUS_CHOICES = (
        ('AtHubUncharged', 'AtHubUncharged'),
        ('AtHubCharged', 'AtHubCharged'),
        ('SignedOut', 'SignedOut'),
        ('Charging', 'Charging'),
        ('Defective', 'Defective'),
        ('Lost', 'Lost'),

    )
    pack_id = models.CharField(
        primary_key=True,
        max_length=9,
        validators=[RegexValidator(r'^[0-9]{9}$', 'Pack ID must have 9 digits')]
    )
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    pack_status = models.CharField(max_length=100, choices=PACK_STATUS_CHOICES)
    current_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pack_id}"
