# Generated by Django 2.0.6 on 2018-07-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domsapp', '0010_auto_20180722_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]