# Generated by Django 2.2.9 on 2020-01-23 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200123_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='descr',
            field=models.CharField(max_length=50),
        ),
    ]
