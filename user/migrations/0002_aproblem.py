# Generated by Django 2.2.1 on 2020-08-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aproblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=200)),
                ('a_content', models.TextField()),
                ('a_answer', models.CharField(max_length=50)),
            ],
        ),
    ]