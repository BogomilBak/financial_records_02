from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Currency(models.Model):
    BGN = 'BGN'
    USD = 'USD'
    EUR = 'EUR'

    CURRENCY_CHOICES = [
        (BGN, 'Bulgarian Lev (BGN)'),
        (USD, 'United States Dollar (USD)'),
        (EUR, 'Euro (EUR)'),
    ]

    code = models.CharField(
        max_length=3,
        unique=True,
    )

    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
    )

    def __str__(self):
        return self.code


class Wallet(models.Model):
    MAX_WALLET_NAME_LENGTH = 25

    name = models.CharField(
        max_length=MAX_WALLET_NAME_LENGTH,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'name',)

    def __str__(self):
        return f"{self.user.email}'s {self.name} wallet"

#
# class Category(models.Model):
#     EXPENSE = 'expense'
#     INCOME = 'income'
#     MAX_CATEGORY_NAME_LENGTH = 25
#
#     CATEGORY_TYPE_CHOICES = [
#         (EXPENSE, 'Expense'),
#         (INCOME, 'Income'),
#     ]
#
#     name = models.CharField(
#         max_length=MAX_CATEGORY_NAME_LENGTH
#     )
#
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )
#
#     type = models.CharField(
#         max_length=7,
#         choices=CATEGORY_TYPE_CHOICES,
#     )
#
#     parent = models.ForeignKey(
#         'self',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )
#
#     class Meta:
#         unique_together = ('user', 'name',)
#
#     def __str__(self):
#         return self.name