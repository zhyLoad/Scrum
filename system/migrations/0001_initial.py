# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('version', models.IntegerField(default=1)),
                ('create_id', models.IntegerField(blank=True, default=0)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 5, 9, 7, 9, 52, 676000, tzinfo=utc))),
                ('modify_id', models.IntegerField(blank=True, default=0)),
                ('modify_time', models.DateTimeField(default=datetime.datetime(2018, 5, 9, 7, 9, 52, 676000, tzinfo=utc))),
                ('transaction_id', models.CharField(max_length=100, blank=True)),
                ('server_name', models.CharField(max_length=100, blank=True)),
                ('name', models.CharField(max_length=100, blank=True, default='')),
                ('phone', models.CharField(max_length=100, blank=True, default='')),
                ('account', models.CharField(max_length=100, default='')),
                ('description', models.CharField(max_length=2048, blank=True, default='')),
                ('tenant_status', models.SmallIntegerField(default=1, choices=[(0, 'has been frozen'), (1, 'has been activated')])),
                ('delete_flag', models.SmallIntegerField(default=1, choices=[(0, 'invalid'), (1, 'valid')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
