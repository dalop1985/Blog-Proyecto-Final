# Generated by Django 4.1.3 on 2023-01-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0006_alter_post_cuerpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resumen',
            field=models.CharField(default='Ingresar un Resumen', max_length=255),
        ),
    ]
