# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(blank=True, null=True, to='store.ProductCategory')),
            ],
            options={
                'verbose_name_plural': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='store.ProductCategory')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
