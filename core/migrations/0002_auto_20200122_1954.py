# Generated by Django 2.2.9 on 2020-01-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbs_down',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbs_up',
            field=models.IntegerField(default=0),
        ),
    ]