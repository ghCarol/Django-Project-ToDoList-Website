# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

from django.db import models


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class ToDoListModel(models.Model):  # todo 数据库中的ToDoListModel表
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    finished = models.BooleanField(default='0')

    # 改名
    # class Meta():
    #     db_table = 'ToDoList'
