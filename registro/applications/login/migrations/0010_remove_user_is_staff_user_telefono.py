# Generated by Django 4.0.6 on 2022-08-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_remove_user_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]
