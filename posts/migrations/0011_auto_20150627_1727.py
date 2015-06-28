# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20150627_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
