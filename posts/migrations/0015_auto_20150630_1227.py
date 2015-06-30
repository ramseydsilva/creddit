# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20150630_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='first_parent',
            field=models.ForeignKey(related_name='all_children', blank=True, to='posts.Post', null=True),
        ),
    ]
