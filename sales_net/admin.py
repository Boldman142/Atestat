from django.contrib import admin
from sales_net.models import SalesNet


@admin.register(SalesNet)
class SalesNetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'provider', 'title', 'levels', 'country', 'city', 'debt', 'created_at')
    list_filter = ('city', 'country',)
    search_fields = ('levels', 'product', 'country')
    actions = ['cleanup_debt']

    def cleanup_debt(self, request, queryset):
        """Очистка задолженности (debt)"""
        for supply_object in queryset:
            supply_object.debt = 0
            supply_object.save()
        self.message_user(request, f'Задолженность у выбранных клиентов очищена.')

    cleanup_debt.short_description = 'Очистить задолженность'
