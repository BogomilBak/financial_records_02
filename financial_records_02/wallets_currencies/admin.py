from django.contrib import admin

from financial_records_02.wallets_currencies.models import Currency, Wallet


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
