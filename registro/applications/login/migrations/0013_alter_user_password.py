# Generated by Django 4.0.6 on 2022-08-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_alter_user_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]