# Generated by Django 4.1.3 on 2023-01-07 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0002_post_titulo_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
