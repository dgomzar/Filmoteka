# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_title', models.CharField(max_length=150, verbose_name='Tytu\u0142 oryginalny')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Tytu\u0142')),
                ('director', models.CharField(blank=True, max_length=100, verbose_name='Re\u017cyseria')),
                ('writer', models.CharField(blank=True, max_length=100, verbose_name='Scenariusz')),
                ('genres', models.CharField(blank=True, max_length=300, verbose_name='Gatunek')),
                ('producer', models.CharField(blank=True, max_length=100, verbose_name='Produkcja')),
                ('release_year', models.CharField(blank=True, max_length=5, null=True, verbose_name='Rok produkcji')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Opis')),
                ('filmweb_rate', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ocena z filmwebu')),
            ],
        ),
    ]