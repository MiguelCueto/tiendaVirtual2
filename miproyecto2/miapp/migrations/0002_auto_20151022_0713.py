# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('tipo', models.CharField(max_length=1, choices=[('N', 'Nuevo'), ('U', 'Usado')])),
            ],
        ),
        migrations.DeleteModel(
            name='ArticuloNuevo',
        ),
        migrations.DeleteModel(
            name='ArticuloUsado',
        ),
    ]
