# Generated by Django 5.0 on 2023-12-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('especie', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=1)),
            ],
        ),
    ]
