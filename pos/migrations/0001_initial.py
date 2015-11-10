# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program_Of_Study',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('advisor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('student_first_name', models.CharField(max_length=200)),
                ('student_last_name', models.CharField(max_length=200)),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='program_of_study',
            name='student',
            field=models.ForeignKey(to='pos.Student'),
        ),
    ]
