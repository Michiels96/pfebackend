# Generated by Django 3.0 on 2019-12-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfants', '0006_enfant_connecte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='connecte',
            field=models.BooleanField(default=False),
        ),
    ]
