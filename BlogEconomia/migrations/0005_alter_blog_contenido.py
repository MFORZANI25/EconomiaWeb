# Generated by Django 3.2.9 on 2022-03-11 14:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogEconomia', '0004_alter_blog_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
