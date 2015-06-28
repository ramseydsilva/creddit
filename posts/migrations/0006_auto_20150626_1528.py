# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150626_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='up',
            field=models.BooleanField(default=False),
        ),
    ]
