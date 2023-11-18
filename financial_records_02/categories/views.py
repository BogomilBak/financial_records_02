from django.shortcuts import render
from rest_framework import generics as api_generics, permissions
from rest_framework import views as api_views

from financial_records_02.categories.models import Category
from financial_records_02.categories.serializers import CategorySerializer
from financial_records_02.utils.permissions import IsOwnerOfAnItemOrObject


class GetUpdateDeleteCategoriesForUser(api_generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)


class CreateGetAllCategoriesForUser(api_generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        IsOwnerOfAnItemOrObject,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
