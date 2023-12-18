# Generated by Django 3.2.22 on 2023-10-31 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20231031_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrollemployee',
            name='status',
        ),
        migrations.AddField(
            model_name='payrollemployee',
            name='age',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payrollemployee',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='account_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='cash',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='cheque_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='gst_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='gst_treatment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='paid_through',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='status',
            field=models.CharField(default='Draft', max_length=100),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='upi_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='paymnt_made_comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasepayment')),
            ],
        ),
    ]