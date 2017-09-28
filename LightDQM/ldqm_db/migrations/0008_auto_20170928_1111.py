# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-28 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ldqm_db', '0007_vfat_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Crate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CrateID', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='run',
            name='amcs',
        ),
        migrations.AddField(
            model_name='amc',
            name='Slot',
            field=models.PositiveSmallIntegerField(default=255),
        ),
        migrations.AddField(
            model_name='geb',
            name='Link',
            field=models.PositiveSmallIntegerField(default=255),
        ),
        migrations.AddField(
            model_name='crate',
            name='amcs',
            field=models.ManyToManyField(to='ldqm_db.AMC'),
        ),
        migrations.AddField(
            model_name='config',
            name='crates',
            field=models.ManyToManyField(to='ldqm_db.Crate'),
        ),
        migrations.AddField(
            model_name='run',
            name='ConfigTag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ldqm_db.Config'),
        ),
    ]