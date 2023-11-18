from django.contrib import admin
from financial_records_02.api_auth.models import FinancialRecordsUser


@admin.register(FinancialRecordsUser)
class FinancialRecordsUserAdmin(admin.ModelAdmin):
    pass
