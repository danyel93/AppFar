# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20150526_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateTimeField(verbose_name=b'fecha de venta'),
        ),
    ]
