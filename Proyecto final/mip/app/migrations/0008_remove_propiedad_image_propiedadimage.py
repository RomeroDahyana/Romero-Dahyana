# Generated by Django 4.2.6 on 2023-11-01 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ciudad_codigo_postal_alter_propiedad_costo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='image',
        ),
        migrations.CreateModel(
            name='PropiedadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='alquilerimg', verbose_name='Imagenes')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.propiedad')),
            ],
        ),
    ]
