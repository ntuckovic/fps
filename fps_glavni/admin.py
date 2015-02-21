from django.contrib import admin

from .models import PoliticalParty, Income, Amount

class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

admin.site.register(PoliticalParty, PoliticalPartyAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

admin.site.register(Income, IncomeAdmin)

class AmountAdmin(admin.ModelAdmin):
    list_display = ['party', 'income', 'amount']
    ordering = ['year', ]

admin.site.register(Amount, AmountAdmin)