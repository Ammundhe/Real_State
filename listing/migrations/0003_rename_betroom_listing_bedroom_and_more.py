# Generated by Django 4.0.3 on 2022-03-28 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_listing_cover_image_listing_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='betroom',
            new_name='bedroom',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='address',
        ),
        migrations.AddField(
            model_name='listing',
            name='Area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='property_status',
            field=models.CharField(blank=True, choices=[('sale', 'sale'), ('rent', 'rent')], default='sale', max_length=255, null=True),
        ),
    ]
