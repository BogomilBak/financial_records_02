from django.contrib import admin

from financial_records_02.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

