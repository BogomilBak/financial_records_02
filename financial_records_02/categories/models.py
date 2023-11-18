from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    EXPENSE = 'expense'
    INCOME = 'income'
    MAX_CATEGORY_NAME_LENGTH = 25

    CATEGORY_TYPE_CHOICES = [
        (EXPENSE, 'Expense'),
        (INCOME, 'Income'),
    ]

    name = models.CharField(
        max_length=MAX_CATEGORY_NAME_LENGTH
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=7,
        choices=CATEGORY_TYPE_CHOICES,
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ('user', 'name',)

    def __str__(self):
        return self.name
