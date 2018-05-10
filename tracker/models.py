# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    def give_a_number(self):
        return 5
