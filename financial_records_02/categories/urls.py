from django.urls import path

from financial_records_02.categories.views import *

urlpatterns = (
    path('/<int:pk>', GetUpdateDeleteCategoriesForUser.as_view(), name='category get update delete'),
    path('', CreateGetAllCategoriesForUser.as_view(), name='category get_all create'),
)