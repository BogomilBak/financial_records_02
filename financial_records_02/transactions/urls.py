from django.urls import path

from financial_records_02.transactions.views import *

urlpatterns = (
    path('/<int:pk>', TransactionsUpdateDeleteGetSpecificForUser.as_view(), name='transaction get update delete'),
    path('', TransactionsGetAllCreateForUser.as_view(), name='transactions get_all create'),
)