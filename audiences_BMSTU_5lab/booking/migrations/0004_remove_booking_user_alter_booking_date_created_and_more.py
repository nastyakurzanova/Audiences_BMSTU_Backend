# Generated by Django 4.2.7 on 2024-01-05 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_audiences_alter_booking_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='description',
            field=models.TextField(blank=True, default='Описание заявки', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(default='Имя заявки', verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
            preserve_default=False,
        ),
    ]
