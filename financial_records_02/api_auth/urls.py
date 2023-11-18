from django.urls import path, include
from financial_records_02.api_auth.views import *

urlpatterns = (
    path('create', RegisterAPIFinancialUserView.as_view(), name='register api user'),
    path('login', LoginAPIFinancialUserView.as_view(), name='login api user'),
)
