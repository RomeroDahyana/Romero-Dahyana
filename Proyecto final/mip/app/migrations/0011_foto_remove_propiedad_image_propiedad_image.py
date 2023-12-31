# Generated by Django 4.2.6 on 2023-11-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_propiedad_ciudad_propiedad_ciudad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='alquilerimg/')),
            ],
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='image',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='image',
            field=models.ManyToManyField(blank=True, to='app.foto'),
        ),
    ]
