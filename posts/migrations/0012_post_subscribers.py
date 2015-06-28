# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20150627_1855'),
        ('posts', '0011_auto_20150627_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribed', through='users.Subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
