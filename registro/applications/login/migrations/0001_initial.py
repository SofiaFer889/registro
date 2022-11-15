# Generated by Django 4.0.6 on 2022-08-27 12:21

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(max_length=40, verbose_name='username')),
                ('nombre', models.CharField(max_length=40, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='apellido')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('tipo', models.IntegerField(choices=[(0, 'admin'), (1, 'superusuario')])),
                ('password', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
