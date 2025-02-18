# Generated by Django 5.1.4 on 2025-01-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_lcdata_applicant_lcdata_expiry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lcdata',
            name='amount',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='lcdata',
            name='beneficiary',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lcdata',
            name='currency',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='lcdata',
            name='tenor',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
