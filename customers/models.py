import uuid
from datetime import timedelta, datetime, timezone

from django.db import models

from customers.fields import PhoneNumberField
from hubs.models import Hub


class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, blank=True, null=True)
    guarantor_first_name = models.CharField(max_length=50, null=True, blank=True)
    guarantor_last_name = models.CharField(max_length=50, null=True, blank=True)
    guarantor_phone = PhoneNumberField(max_length=50, null=True, blank=True)
    membership_expiry_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)

    def update_membership(self, duration):
        now = datetime.now(tz=timezone.utc)
        if not self.membership_expiry_date or self.membership_expiry_date < now:
            self.membership_expiry_date = now + timedelta(days=duration)
        else:
            self.membership_expiry_date += timedelta(days=duration)
        self.save()

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
