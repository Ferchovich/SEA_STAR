# Generated by Django 4.2.5 on 2023-11-10 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0022_remove_reservacamarote_encargadoreservado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recorrido',
            name='listaPasajeros',
        ),
        migrations.RemoveField(
            model_name='recorrido',
            name='listaPuertos',
        ),
    ]