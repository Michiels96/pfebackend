# Generated by Django 3.0 on 2019-12-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfants', '0005_auto_20191205_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='connecte',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
