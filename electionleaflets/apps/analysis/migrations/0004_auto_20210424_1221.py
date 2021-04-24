# Generated by Django 2.2.20 on 2021-04-24 12:21

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_add_missing_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leafletproperties',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='leafletproperties',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
