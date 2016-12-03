# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Sido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'sido',
            },
        ),
        migrations.CreateModel(
            name='Sigungu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('sido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sido_id', to='address.Sido')),
            ],
            options={
                'db_table': 'sigungu',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='Sigungu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sigungu', to='address.Sigungu'),
        ),
    ]
