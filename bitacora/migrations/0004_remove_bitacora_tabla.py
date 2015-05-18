# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0003_remove_bitacora_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitacora',
            name='tabla',
        ),
    ]
