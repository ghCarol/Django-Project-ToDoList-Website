# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0006_auto_20180429_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished',
            field=models.BooleanField(default=b'False'),
        ),
    ]
