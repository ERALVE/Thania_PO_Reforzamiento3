# Generated by Django 5.0 on 2023-12-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=1)),
            ],
        ),
    ]
