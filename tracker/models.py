# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name_text = models.CharField(max_length=200)


class Meal(models.Model):
    name_text = models.CharField(max_length=200)
