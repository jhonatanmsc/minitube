# Generated by Django 2.2.9 on 2020-01-23 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200123_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='descr',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]
