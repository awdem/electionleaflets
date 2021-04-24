# Generated by Django 2.2.20 on 2021-04-24 13:06

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    replaces = [('leaflets', '0001_initial'), ('leaflets', '0002_leaflet_publisher_person'), ('leaflets', '0003_Add orientation and exif data'), ('leaflets', '0004_remove_leafletimage_image_text'), ('leaflets', '0005_add_ynr_ids'), ('leaflets', '0006_add_ynr_idxes'), ('leaflets', '0007_add_ynr_ids'), ('leaflets', '0008_remove_leaflet_location')]

    dependencies = [
        ('elections', '0001_initial'),
        ('people', '0001_initial'),
        ('constituencies', '0001_initial'),
        ('uk_political_parties', '0004_auto_20150322_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaflet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=765)),
                ('description', models.TextField(blank=True, null=True)),
                ('imprint', models.TextField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=150)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_delivered', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('live', 'Live'), ('draft', 'Draft'), ('removed', 'Removed')], max_length=255, null=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('constituency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constituencies.Constituency')),
                ('election', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
                ('publisher_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uk_political_parties.Party')),
                ('publisher_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
                ('ballot_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ynr_party_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ynr_party_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ynr_person_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('ynr_person_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('-date_uploaded',),
            },
        ),
        migrations.CreateModel(
            name='LeafletImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(max_length=255, upload_to='leaflets')),
                ('raw_image', sorl.thumbnail.fields.ImageField(blank=True, max_length=255, upload_to='raw_leaflets')),
                ('legacy_image_key', models.CharField(blank=True, max_length=255)),
                ('image_type', models.CharField(blank=True, choices=[('1_front', 'Front'), ('2_back', 'Back'), ('3_inside', 'Inside'), ('4_inprint', 'Inprint')], max_length=255, null=True)),
                ('leaflet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='leaflets.Leaflet')),
                ('exif_data', models.BinaryField(blank=True, null=True)),
                ('orientation', models.PositiveSmallIntegerField(choices=[(1, 'Horizontal (normal)'), (2, 'Mirror horizontal'), (3, 'Rotate 180'), (4, 'Mirror vertical'), (5, 'Mirror horizontal and rotate 270 CW'), (6, 'Rotate 90 CW'), (7, 'Mirror horizontal and rotate 90 CW'), (8, 'Rotate 270 CW')], default=1)),
            ],
            options={
                'ordering': ['image_type'],
            },
        ),
    ]
