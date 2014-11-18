# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField(null=True, blank=True)),
                ('category', models.CharField(max_length=20)),
                ('bodytext', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
