# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hostel_fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=30, choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')])),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mess_deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=30, choices=[('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('may', 'April'), ('apr', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sep', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'December')])),
                ('bill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('usn', models.CharField(max_length=10)),
                ('email', models.EmailField()),
                ('profile_picture', models.ImageField(upload_to=b'profile_pics/', blank=True, null=True)),
                ('hostel_fee_paid', models.ManyToManyField(to='students.hostel_fee', blank=True)),
                ('mess_bill_paid', models.ManyToManyField(to='students.mess_deposit', blank=True)),
                ('fine_student', models.ManyToManyField(to='students.fine', blank=True)),
            ],
            options={
                'ordering': ['usn'],
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'files/', validators=[<function validate_file_extension at 0x7f8b8c0d3e18>])),
                ('name', models.CharField(default=b'tempfile', max_length=30)),
            ],
        ),
    ]