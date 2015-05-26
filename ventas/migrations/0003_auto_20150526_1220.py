# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20150526_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateTimeField(auto_now=True, verbose_name=b'fecha de venta'),
        ),
    ]
