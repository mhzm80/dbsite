# Generated by Django 4.2.1 on 2023-05-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noskhe_h',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(max_length=10)),
                ('Ideadoctor', models.TextField()),
            ],
        ),
    ]