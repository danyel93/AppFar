# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(verbose_name=b'fecha de venta')),
                ('total', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(to='cliente.cliente')),
                ('medicamento_s', models.ManyToManyField(to='medicamento.medicamento')),
                ('vendedor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
