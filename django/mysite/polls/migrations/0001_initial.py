# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_name', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'vehicle',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_brand_id', models.IntegerField(null=True, blank=True)),
                ('vehicle_brand_name', models.CharField(max_length=100, blank=True)),
                ('vehicle_brand_description', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'vehicle_brand',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_country_name', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'vehicle_country',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_model_id', models.IntegerField(null=True, blank=True)),
                ('vehicle_model_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('vehicle_brand_id', models.ForeignKey(to='polls.VehicleBrand', db_column=b'vehicle_brand_id')),
                ('vehicle_country_id', models.ForeignKey(to='polls.VehicleCountry', db_column=b'vehicle_country_id')),
            ],
            options={
                'db_table': 'vehicle_model',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_type_id', models.IntegerField(default=b'', null=True, blank=True)),
                ('vehicle_type_name', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'vehicle_type',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vehiclebrand',
            name='vehicle_country',
            field=models.OneToOneField(to='polls.VehicleCountry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_brand_id',
            field=models.ForeignKey(to='polls.VehicleBrand', db_column=b'vehicle_brand_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_country_id',
            field=models.ForeignKey(to='polls.VehicleCountry', db_column=b'vehicle_country_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model_id',
            field=models.ForeignKey(to='polls.VehicleModel', db_column=b'vehicle_model_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type_id',
            field=models.ForeignKey(db_column=b'vehicle_type_id', default=b'', to='polls.VehicleType'),
            preserve_default=True,
        ),
    ]
