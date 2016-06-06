# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0019_auto_20160605_1905'),
        ('uclptb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='date_of_death',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='death_indicator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='demographics',
            name='gp_practice_code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='marital_status_fk',
            field=models.ForeignKey(blank=True, to='opal.MaritalStatus', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='marital_status_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='post_code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='religion',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='title_fk',
            field=models.ForeignKey(blank=True, to='opal.Title', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='title_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='middle_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
