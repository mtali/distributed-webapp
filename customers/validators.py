from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.startswith('0'):
        raise ValidationError('Phone number must start with 0')
    if len(value) != 10:
        raise ValidationError('Phone number must have 10 digits')
