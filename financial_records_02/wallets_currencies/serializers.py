from django.contrib.auth import get_user_model
from rest_framework import serializers

from financial_records_02.transactions.models import Transactions
from financial_records_02.wallets_currencies.models import Wallet, Currency

UserModel = get_user_model()


class WalletGeneralSerializer(serializers.ModelSerializer):
    currency_id = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(),
        write_only=True,
        allow_null=True,
        source='currency'
    )

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'currency_id')

    def to_internal_value(self, data):
        currency_id = data.get('currency_id')
        if currency_id:
            data['currency'] = currency_id

        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_id'] = instance.user.id
        return representation





