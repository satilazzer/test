# Generated by Django 3.2.4 on 2023-08-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230817_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='user_tg_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
