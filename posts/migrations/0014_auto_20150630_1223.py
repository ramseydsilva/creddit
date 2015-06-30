# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_first_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='first_parent',
            field=models.ForeignKey(related_name='all_children', default=1, to='posts.Post'),
            preserve_default=False,
        ),
    ]
