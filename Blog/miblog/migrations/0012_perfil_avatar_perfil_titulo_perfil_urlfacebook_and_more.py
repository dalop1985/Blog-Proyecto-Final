# Generated by Django 4.1.3 on 2023-01-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0011_alter_post_resumen_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/perfil/'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='titulo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='urlfacebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='urlpersonal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='urltwitter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]