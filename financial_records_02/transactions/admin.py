from django.contrib import admin

from financial_records_02.transactions.models import Transactions


@admin.register(Transactions)
class AdminTransactions(admin.ModelAdmin):
    pass
