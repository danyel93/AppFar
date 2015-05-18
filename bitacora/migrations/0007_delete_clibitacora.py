# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0006_clibitacora'),
    ]

    operations = [
        migrations.DeleteModel(
            name='clibitacora',
        ),
    ]
