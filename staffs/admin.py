from django.contrib import admin

from staffs.models import Staff


# noinspection PyMethodMayBeStatic
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('customer__hub', 'created_at',)

    def full_name(self, instance):
        return f"{instance.customer}"
