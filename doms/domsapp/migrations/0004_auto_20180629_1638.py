# Generated by Django 2.0.6 on 2018-06-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domsapp', '0003_auto_20180629_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='comments',
            field=models.TextField(),
        ),
    ]
