from rest_framework import serializers

from financial_records_02.categories.models import Category
from financial_records_02.transactions.models import Transactions
from financial_records_02.wallets_currencies.models import Wallet


class TransactionsGeneralSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        allow_null=True,
        source='category'
    )

    wallet_id = serializers.PrimaryKeyRelatedField(
        queryset=Wallet.objects.all(),
        write_only=True,
        allow_null=True,
        source='wallet'
    )

    class Meta:
        model = Transactions
        fields = ('id', 'wallet_id', 'category_id', 'amount', 'description')

        def create(self, validated_data):
            user = self.context['request'].user  # Get the authenticated user from the request
            transaction = Transactions.objects.create(user=user, **validated_data)
            return transaction

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_id'] = instance.user.id
        representation['wallet_id'] = instance.wallet.id
        representation['category_id'] = instance.category.id
        return representation

