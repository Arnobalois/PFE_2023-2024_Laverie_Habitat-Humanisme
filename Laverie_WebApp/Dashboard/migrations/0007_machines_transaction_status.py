# Generated by Django 4.2.7 on 2023-12-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_remove_locataires_nom_remove_locataires_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='transaction_status',
            field=models.CharField(choices=[('Sèche Linge', 'Seche Linge'), ('Lave Linge', 'Lave Linge')], default='Lave Linge', max_length=255),
        ),
    ]
