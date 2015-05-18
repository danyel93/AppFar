# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0007_delete_clibitacora'),
    ]

    operations = [
        migrations.CreateModel(
            name='clibita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=50)),
                ('operacion', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('campo', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
