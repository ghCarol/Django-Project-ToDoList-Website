# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0005_auto_20180423_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField(null=True)),
                ('finished', models.BooleanField(default=b'0')),
            ],
            options={
                'db_table': 'Task',
            },
        ),
        migrations.DeleteModel(
            name='ToDoListModel',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
