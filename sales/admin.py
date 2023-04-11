from django.contrib import admin

from sales.models import Membership, Transaction


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_in_days', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount', 'pack_in', 'pack_out', 'type', 'duration_in_days', 'created_at', 'updated_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__phone', 'pack_in', 'pack_out', 'type')
    list_filter = ('customer__hub__name', 'type', 'created_at', 'updated_at',)
