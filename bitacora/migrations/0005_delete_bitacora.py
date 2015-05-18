# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0004_remove_bitacora_tabla'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bitacora',
        ),
    ]
