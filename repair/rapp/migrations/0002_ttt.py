# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTT',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('last_name', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
                'db_table': 'test_ttt',
            },
        ),
    ]
