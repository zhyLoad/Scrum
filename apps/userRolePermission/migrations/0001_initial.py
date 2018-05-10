# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PermissionsRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('permission', models.ForeignKey(to='userRolePermission.Permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TokenUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('token', models.CharField(max_length=512)),
                ('created', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role', models.ForeignKey(to='userRolePermission.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('created', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='userroles',
            name='user',
            field=models.ForeignKey(to='userRolePermission.Users'),
        ),
        migrations.AddField(
            model_name='tokenusers',
            name='user',
            field=models.ForeignKey(to='userRolePermission.Users'),
        ),
        migrations.AddField(
            model_name='permissionsroles',
            name='role',
            field=models.ForeignKey(to='userRolePermission.Roles'),
        ),
    ]
