# Generated by Django 4.2.7 on 2023-12-18 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_alter_machines_numero_machine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='Numero_Capteur',
            new_name='ID_Capteur',
        ),
    ]
