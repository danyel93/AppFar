# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0008_clibita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clibita',
            name='usuario',
            field=models.IntegerField(),
        ),
    ]
