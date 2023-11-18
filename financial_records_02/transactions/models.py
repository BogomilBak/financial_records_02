from django.contrib.auth import get_user_model
from django.db import models
from financial_records_02.wallets_currencies.models import Wallet
from financial_records_02.categories.models import Category
UserModel = get_user_model()


class Transactions(models.Model):
    DESCRIPTION_NAME_MAX_LENGTH = 255

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    transaction_date = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.CharField(
        max_length=DESCRIPTION_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"Transaction by {self.user.email} - {self.transaction_date} for {self.amount}"
