# Generated by Django 4.2.5 on 2023-11-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0020_reservacamarote_recorridoreservado'),
    ]

    operations = [
        migrations.AddField(
            model_name='camarote',
            name='navioUbicado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seastar.navio'),
            preserve_default=False,
        ),
    ]
