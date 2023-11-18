from django.contrib.auth import get_user_model, login, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics as generic_api_views, permissions, status
from rest_framework import views as api_views

from financial_records_02.api_auth.serializer import CreateAPIFinancialUserSerializer

UserModel = get_user_model()


class RegisterAPIFinancialUserView(generic_api_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateAPIFinancialUserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginAPIFinancialUserView(api_views.APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
