# Generated by Django 4.0.6 on 2022-08-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
