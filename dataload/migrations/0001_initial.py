# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionRecordElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True, blank=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('element_type', models.CharField(blank=True, max_length=2, null=True, choices=[(b'da', b'transaction date'), (b'tt', b'transaction type'), (b'na', b'name'), (b'na', b'memo'), (b'tr', b'transaction amount')])),
                ('date_format', models.CharField(max_length=256, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
