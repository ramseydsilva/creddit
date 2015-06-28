# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150626_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('-credit',)},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='score',
            new_name='credit',
        ),
    ]
