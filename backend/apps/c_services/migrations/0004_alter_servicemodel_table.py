# Generated by Django 4.1.7 on 2023-02-21 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c_services', '0003_rename_service_photos_photoservicemodel_photos_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='servicemodel',
            table='services',
        ),
    ]