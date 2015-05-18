# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0010_delete_clibita'),
    ]

    operations = [
        migrations.CreateModel(
            name='informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operacion', models.CharField(max_length=1)),
                ('fecha', models.DateField(auto_now=True)),
                ('usuario', models.CharField(max_length=50)),
                ('campo', models.CharField(max_length=50)),
                ('atributo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
