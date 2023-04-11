from django.core.validators import RegexValidator
from django.db import models

from customers.validators import validate_phone_number


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validators', []).extend([
            RegexValidator(r'^\d{10}$', 'Phone number must have 10 digits'),
            validate_phone_number
        ])
        super().__init__(*args, **kwargs)
