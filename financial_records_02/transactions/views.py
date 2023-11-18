from financial_records_02.transactions.models import Transactions
from financial_records_02.transactions.serializers import TransactionsGeneralSerializer
from financial_records_02.utils.permissions import IsOwnerOfAnItemOrObject
from rest_framework import generics as api_generics, permissions
from rest_framework import generics as api_generics, permissions

from financial_records_02.transactions.models import Transactions
from financial_records_02.utils.permissions import IsOwnerOfAnItemOrObject


class TransactionsGetAllCreateForUser(api_generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsGeneralSerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Transactions.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionsUpdateDeleteGetSpecificForUser(api_generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsGeneralSerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Transactions.objects.filter(user=user)