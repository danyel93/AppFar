# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.IntegerField(default=2, choices=[(1, b'Adulto'), (2, b'Infatil')])),
                ('presentacion', models.IntegerField(default=3, choices=[(1, b'Tabletas'), (2, b'Jarabe'), (3, b'Pomada')])),
                ('precio', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to=b'Imagenes')),
                ('caducidad', models.DateField()),
                ('laboratorio', models.ForeignKey(to='laboratorio.laboratorio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
