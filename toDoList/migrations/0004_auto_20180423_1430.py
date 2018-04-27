# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0003_auto_20180423_1430'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todolist',
            table='ToDoList',
        ),
    ]
