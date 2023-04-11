from django.db import models

from customers.models import Customer


class Staff(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True, editable=True)
    is_active = models.BooleanField(default=True)
    pin = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"

    class Meta:
        db_table = 'staffs'
