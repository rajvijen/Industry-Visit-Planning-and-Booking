# Generated by Django 2.1.3 on 2018-12-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_bookinglistindi_left_days_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinglistindi',
            name='industry_branch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookinglistorga',
            name='industry_branch',
            field=models.CharField(max_length=100, null=True),
        ),
    ]