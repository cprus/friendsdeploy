# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import users
from django.db import models


class friends(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    flist = models.ForeignKey(users, related_name="friends")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
