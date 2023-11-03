# Generated by Django 4.2.5 on 2023-10-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0011_remove_solicitudviaje_pasajero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cubierta',
            name='camarote',
        ),
        migrations.AddField(
            model_name='camarote',
            name='cubiertaUbicada',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seastar.cubierta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cubierta',
            name='navioUbicado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seastar.navio'),
            preserve_default=False,
        ),
    ]