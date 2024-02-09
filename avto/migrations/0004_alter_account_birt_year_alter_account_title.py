# Generated by Django 5.0.2 on 2024-02-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birt_year',
            field=models.CharField(choices=[('ninty_eight', '1998'), ('ninty_nine', '1999'), ('two_thousand', '2000'), ('th_one', '2001')], max_length=12),
        ),
        migrations.AlterField(
            model_name='account',
            name='title',
            field=models.CharField(default='id', max_length=128),
        ),
    ]