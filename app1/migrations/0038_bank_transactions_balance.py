# Generated by Django 3.2.22 on 2023-11-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_auto_20231114_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transactions',
            name='balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]