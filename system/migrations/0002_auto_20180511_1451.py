# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 6, 51, 9, 105365, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 6, 51, 9, 105365, tzinfo=utc)),
        ),
    ]
