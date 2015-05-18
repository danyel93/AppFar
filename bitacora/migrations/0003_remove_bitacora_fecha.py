# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0002_auto_20150517_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitacora',
            name='fecha',
        ),
    ]
