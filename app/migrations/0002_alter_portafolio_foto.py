# Generated by Django 4.1.4 on 2022-12-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='foto',
            field=models.ImageField(null=True, upload_to='portafolio'),
        ),
    ]
