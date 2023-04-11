from django.db import models


class Hub(models.Model):
    name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hubs'

    def __str__(self):
        return self.name
