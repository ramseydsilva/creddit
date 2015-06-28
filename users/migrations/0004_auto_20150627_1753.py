# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20150627_1727'),
        ('users', '0003_auto_20150627_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='posts.Post')),
                ('user', models.ForeignKey(to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='subscribed',
            field=models.ManyToManyField(related_name='subscribers', through='users.Subscription', to='posts.Post'),
        ),
    ]
