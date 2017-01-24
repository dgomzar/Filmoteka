# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
    org_title = models.CharField(max_length=150, blank=False, verbose_name=(u"Tytuł oryginalny"))
    title = models.CharField(max_length=150, blank=True, verbose_name=(u"Tytuł"))
    director = models.CharField(max_length=100, blank=True, verbose_name=(u"Reżyseria"))
    writer = models.CharField(max_length=100, blank=True, verbose_name=(u"Scenariusz"))
    genres = models.CharField(max_length=300, blank=True, verbose_name=(u"Gatunek"))
    producer = models.CharField(max_length=100, blank=True, verbose_name=(u"Produkcja"))
    release_year = models.CharField(max_length=5, blank=True, null=True, verbose_name=(u"Rok produkcji"))
    description = models.CharField(max_length=1000, blank=True, verbose_name=(u"Opis"))
    filmweb_rate = models.CharField(max_length=10, blank=True, null=True, verbose_name=(u"Ocena z filmwebu"))
