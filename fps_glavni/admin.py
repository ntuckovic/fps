from django.contrib import admin

from .models import PoliticalParty, Income, Amount

class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    prepopulated_fields = {'slug': ('short_name',)}

admin.site.register(PoliticalParty, PoliticalPartyAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Income, IncomeAdmin)

class AmountAdmin(admin.ModelAdmin):
    list_display = ['party', 'income', 'amount', 'year']
    list_filter = ['party', 'income', 'year']
    list_editable = ['income', 'amount', 'year']
    ordering = ['year', 'income']

admin.site.register(Amount, AmountAdmin)