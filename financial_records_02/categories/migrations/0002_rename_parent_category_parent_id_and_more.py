# Generated by Django 4.2.6 on 2023-10-25 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='parent_id',
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='category',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('user_id', 'name')},
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]