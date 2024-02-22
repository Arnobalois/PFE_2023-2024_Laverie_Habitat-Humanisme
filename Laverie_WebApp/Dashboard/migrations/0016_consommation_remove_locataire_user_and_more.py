# Generated by Django 4.2.7 on 2024-02-22 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0015_machine_selectiondate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consommation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comsumption_date', models.DateTimeField(null=True)),
                ('comsumption_duration', models.IntegerField(null=True)),
                ('comsumption', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='locataire',
            name='user',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='SelectionDate',
        ),
        migrations.AddField(
            model_name='machine',
            name='RemainingTime',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Consomation',
        ),
        migrations.DeleteModel(
            name='Locataire',
        ),
        migrations.AddField(
            model_name='consommation',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.machine'),
        ),
        migrations.AddField(
            model_name='consommation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
