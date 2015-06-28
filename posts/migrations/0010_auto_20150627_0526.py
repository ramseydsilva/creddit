# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_auto_20150626_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.RemoveField(
            model_name='view',
            name='post',
        ),
        migrations.RemoveField(
            model_name='view',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='post',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-credit', '-created_date')},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='score',
            new_name='credit',
        ),
        migrations.DeleteModel(
            name='View',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.AddField(
            model_name='hit',
            name='post',
            field=models.ForeignKey(to='posts.Post'),
        ),
        migrations.AddField(
            model_name='hit',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='credit',
            name='post',
            field=models.ForeignKey(related_name='credit_set', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='credit',
            unique_together=set([('user', 'post')]),
        ),
    ]
