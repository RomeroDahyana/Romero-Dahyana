# Generated by Django 4.2.6 on 2023-11-01 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_propiedad_image_delete_propiedadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='ciudad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.ciudad', verbose_name='Ciudad'),
        ),
    ]
