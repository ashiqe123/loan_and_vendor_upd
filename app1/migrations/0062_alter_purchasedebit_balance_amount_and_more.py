# Generated by Django 4.2.5 on 2023-12-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0061_alter_purchasepayment_amtreceived_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedebit',
            name='balance_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='paid_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
