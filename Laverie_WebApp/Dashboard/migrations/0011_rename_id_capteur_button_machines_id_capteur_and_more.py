# Generated by Django 4.2.7 on 2023-12-21 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0010_rename_id_capteur_machines_id_capteur_button_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='ID_Capteur_Button',
            new_name='ID_Capteur',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='ID_Capteur_Current',
        ),
    ]
