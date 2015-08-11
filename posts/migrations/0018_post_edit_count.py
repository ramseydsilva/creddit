# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20150630_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edit_count',
            field=models.IntegerField(default=0),
        ),
    ]
