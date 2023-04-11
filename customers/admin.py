from django.contrib import admin

from customers.models import Customer


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'phone', 'created_at')
    list_filter = ('hub__name', 'created_at')
    search_fields = (
        'first_name',
        'last_name',
        'phone',
        'gender',
        'guarantor_first_name',
        'guarantor_last_name',
        'guarantor_phone'
    )
