# Generated by Django 4.2 on 2023-04-11 10:53

import django.core.validators
from django.db import migrations

import customers.fields
import customers.validators


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0003_alter_customer_guarantor_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='guarantor_phone',
            field=customers.fields.PhoneNumberField(blank=True, max_length=50, null=True, validators=[
                django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must have 10 digits'),
                customers.validators.validate_phone_number,
                django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must have 10 digits'),
                customers.validators.validate_phone_number]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=customers.fields.PhoneNumberField(max_length=50, validators=[
                django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must have 10 digits'),
                customers.validators.validate_phone_number,
                django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must have 10 digits'),
                customers.validators.validate_phone_number]),
        ),
    ]
