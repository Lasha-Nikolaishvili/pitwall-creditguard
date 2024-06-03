from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'censored_number', 'is_valid', 'created_at')
    list_filter = ('is_valid', 'created_at')
    search_fields = ('title', 'censored_number')
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'censored_number', 'is_valid')
        }),
        (_('Date Information'), {
            'fields': ('created_at',)
        }),
    )
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
