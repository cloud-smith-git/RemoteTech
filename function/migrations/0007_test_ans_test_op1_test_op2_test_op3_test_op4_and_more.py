# Generated by Django 5.0.1 on 2024-02-19 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0006_alter_fuelpurchase_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='ans',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='op1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='op2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='op3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='op4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='question',
            field=models.CharField(max_length=200, null=True),
        ),
    ]