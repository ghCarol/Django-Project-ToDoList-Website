# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0004_auto_20180423_1430'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='ToDoListModel',
        ),
        migrations.AlterModelTable(
            name='todolistmodel',
            table=None,
        ),
    ]
