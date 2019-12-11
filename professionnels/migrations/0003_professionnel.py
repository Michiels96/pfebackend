# Generated by Django 3.0 on 2019-12-10 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professionnels', '0002_delete_professionnel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professionnel',
            fields=[
                ('professionnel_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=42)),
                ('prenom', models.CharField(max_length=42)),
                ('profession', models.CharField(choices=[('Erg', 'Ergothérapeute'), ('Psy', 'Psychologue'), ('Ed', 'Educateur'), ('Ki', 'Kinésithérapeute'), ('En', 'Enseignant'), ('Au', 'Autre')], max_length=42, null=True)),
                ('autre_profession', models.CharField(max_length=42, null=True)),
                ('telephone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]