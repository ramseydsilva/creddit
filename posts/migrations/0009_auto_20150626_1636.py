# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20150626_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
