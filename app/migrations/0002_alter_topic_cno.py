# Generated by Django 4.1.7 on 2023-04-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='cno',
            field=models.IntegerField(),
        ),
    ]
