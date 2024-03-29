# Generated by Django 4.0.3 on 2022-04-13 15:34

from django.db import migrations
from django.utils.text import slugify


def popular_slugs(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slugs)
    ]
