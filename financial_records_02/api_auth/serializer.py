from django.contrib.auth import get_user_model
from rest_framework import generics as api_views, serializers
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class CreateAPIFinancialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result
