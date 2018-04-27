# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('finished', models.BooleanField()),
            ],
        ),
    ]
