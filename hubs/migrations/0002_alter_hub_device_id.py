# Generated by Django 4.2 on 2023-04-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='device_id',
            field=models.CharField(default='Hello', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
