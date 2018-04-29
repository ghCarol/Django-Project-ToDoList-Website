# -*- coding: UTF-8 -*-
# Create your models here.

from django.db import models


class Task(models.Model):  # todo 数据库中的ToDoListModel表
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    finished = models.BooleanField(default='0')

    # 改名
    class Meta():
         db_table = 'Task'
