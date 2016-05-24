# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0002_ttt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
