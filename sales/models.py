import uuid

from django.db import models

from customers.models import Customer
from packs.models import Pack


class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'memberships'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('Swap', 'Swap'),
        ('Membership', 'Membership')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pack_in = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name="transactions_in", blank=True, null=True)
    pack_out = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name="transactions_out", blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    duration_in_days = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"{self.customer} - {self.type}"
