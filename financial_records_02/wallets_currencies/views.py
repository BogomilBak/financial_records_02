from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics as generic_apic_views, permissions
from rest_framework import views as api_views
from rest_framework.response import Response

from financial_records_02.utils.permissions import IsOwnerOfAnItemOrObject
from financial_records_02.wallets_currencies.models import Wallet, Currency
from financial_records_02.wallets_currencies.serializers import WalletGeneralSerializer

UserModel = get_user_model()


class WalletGetUpdateDeleteByIDForUser(generic_apic_views.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletGeneralSerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)


class WalletCreateGetAllForUser(generic_apic_views.ListCreateAPIView):

    queryset = Wallet.objects.all()
    serializer_class = WalletGeneralSerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




