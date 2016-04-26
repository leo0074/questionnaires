# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaires', '0006_auto_20160424_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Old_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('min', models.IntegerField(default=0)),
                ('max', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='current_version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='old_questions',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionnaires.Question'),
        ),
    ]
