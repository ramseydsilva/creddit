# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20150626_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-score', '-created_date')},
        ),
        migrations.RemoveField(
            model_name='vote',
            name='down',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='up',
        ),
        migrations.AddField(
            model_name='vote',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
