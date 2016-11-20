# -*- coding: utf-8 -*-
from django.db import models


class ModifiedModel(models.Model):
    created = models.DateTimeField("Erstellt am", default=datetime.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)