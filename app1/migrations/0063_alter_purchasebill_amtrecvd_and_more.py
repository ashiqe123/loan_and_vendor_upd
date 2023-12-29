# Generated by Django 4.2.5 on 2023-12-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0062_alter_purchasedebit_balance_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill',
            name='amtrecvd',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='balance_due',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='amtrecvd',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='balance_amount',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='paid_amount',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasepayment',
            name='amtcredit',
            field=models.FloatField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='purchasepayment',
            name='amtreceived',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasepayment',
            name='paymentamount',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='balance',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='paid_amount',
            field=models.FloatField(default=0, max_length=100, null=True),
        ),
    ]
