from django.urls import path
from financial_records_02.wallets_currencies.views import *

urlpatterns = (
        path('', WalletCreateGetAllForUser.as_view(), name='wallets get_all create'),
        path('/<int:pk>', WalletGetUpdateDeleteByIDForUser.as_view(), name='wallets get_byid update delete'),
    )
