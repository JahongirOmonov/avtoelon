# Generated by Django 5.0.2 on 2024-02-09 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('birt_year', models.CharField(choices=[('1998', 'Ninty Eight'), ('1999', 'Ninty Nine'), ('2000', 'Two Thousand'), ('2001', 'Th One')], max_length=4)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avto.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avto.region')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]