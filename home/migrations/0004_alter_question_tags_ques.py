# Generated by Django 3.2 on 2021-04-27 14:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_tags_question_tags_ques'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags_ques',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None, verbose_name='Tags for Question'),
        ),
    ]
