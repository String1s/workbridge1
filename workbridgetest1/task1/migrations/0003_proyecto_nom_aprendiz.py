# Generated by Django 4.1.5 on 2024-06-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='nom_aprendiz',
            field=models.CharField(default='Aprendiz Desconocido', max_length=200),
        ),
    ]
