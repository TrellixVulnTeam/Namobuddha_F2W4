# Generated by Django 2.0.6 on 2018-07-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domsapp', '0009_auto_20180722_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to='media'),
        ),
    ]
