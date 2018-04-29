# -*- coding: UTF-8 -*-
# Create your models here.

from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    finished = models.BooleanField(default='False')  # 原来是='0'

    # 改名
    class Meta():
        db_table = 'Task'
