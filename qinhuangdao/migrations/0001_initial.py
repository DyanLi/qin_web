# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-04-24 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qinhuangdao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('direction1', models.IntegerField()),
                ('velocity1', models.FloatField()),
                ('direction2', models.IntegerField()),
                ('velocity2', models.FloatField()),
                ('direction3', models.IntegerField()),
                ('velocity3', models.FloatField()),
                ('direction4', models.IntegerField()),
                ('velocity4', models.FloatField()),
                ('direction5', models.IntegerField()),
                ('velocity5', models.FloatField()),
                ('direction6', models.IntegerField()),
                ('velocity6', models.FloatField()),
                ('direction7', models.IntegerField()),
                ('velocity7', models.FloatField()),
                ('direction8', models.IntegerField()),
                ('velocity8', models.FloatField()),
                ('direction9', models.IntegerField()),
                ('velocity9', models.FloatField()),
                ('direction10', models.IntegerField()),
                ('velocity10', models.FloatField()),
                ('direction11', models.IntegerField()),
                ('velocity11', models.FloatField()),
                ('direction12', models.IntegerField()),
                ('velocity12', models.FloatField()),
                ('direction13', models.IntegerField()),
                ('velocity13', models.FloatField()),
                ('direction14', models.IntegerField()),
                ('velocity14', models.FloatField()),
                ('direction15', models.IntegerField()),
                ('velocity15', models.FloatField()),
            ],
        ),
    ]
