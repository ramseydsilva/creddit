# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150626_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='children',
        ),
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='posts.Post', null=True),
        ),
    ]
