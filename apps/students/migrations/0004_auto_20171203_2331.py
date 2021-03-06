# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20171203_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=1, verbose_name='género'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='edad'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(verbose_name='fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_code',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='código tarjeta'),
        ),
        migrations.AlterField(
            model_name='student',
            name='career',
            field=models.CharField(choices=[('AI', 'Administración Industrial'), ('II', 'Ingeniería Industrial'), ('IT', 'Ingeniería en Transporte'), ('IN', 'Ingeniería en Informática'), ('CI', 'Ciencias de la Informática')], max_length=2, verbose_name='carrera'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=80, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_surname',
            field=models.CharField(max_length=30, verbose_name='apellido paterno'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='second_surname',
            field=models.CharField(max_length=30, verbose_name='apellido materno'),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1, verbose_name='semestre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='boleta'),
        ),
        migrations.AlterField(
            model_name='student',
            name='telephone',
            field=models.CharField(max_length=10, verbose_name='teléfono'),
        ),
    ]
