# Generated by Django 5.0.1 on 2024-02-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0004_rename_taillights_vehiclecheck_tail_lights'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelpurchase',
            name='image',
            field=models.ImageField(blank=True, default='None', upload_to=None),
        ),
    ]
