# Generated by Django 4.2 on 2023-06-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhook',
            name='type',
            field=models.CharField(
                choices=[('SwapSale', 'SwapSale'), ('NewUser', 'NewUser'), ('UpdateUser', 'UpdateUser'),
                         ('MembershipSale', 'MembershipSale'), ('PackUpdate', 'PackUpdate')], max_length=100),
        ),
    ]
