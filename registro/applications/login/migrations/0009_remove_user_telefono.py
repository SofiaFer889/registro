# Generated by Django 4.0.6 on 2022-08-31 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telefono',
        ),
    ]