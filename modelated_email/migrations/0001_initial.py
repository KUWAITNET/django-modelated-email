# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(max_length=128, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z_][0-9a-zA-Z_]*$', message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.")], help_text='Code used for looking up this event programmatically', unique=True, verbose_name='Code')),
                ('name', models.CharField(help_text='This is just used for organisational purposes', max_length=255, verbose_name='Name')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Email template',
                'verbose_name_plural': 'Email templates',
            },
        ),
    ]
