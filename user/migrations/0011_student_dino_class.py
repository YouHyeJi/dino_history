# Generated by Django 2.2.4 on 2020-10-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20201017_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dino_class',
            field=models.IntegerField(default=0),
        ),
    ]