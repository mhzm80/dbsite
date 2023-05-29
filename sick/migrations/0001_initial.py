# Generated by Django 4.2.1 on 2023-05-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Age', models.IntegerField(default=0)),
                ('Nationalcode', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Phonenumber', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Context', models.TextField()),
                ('Drname', models.CharField(max_length=200)),
                ('Insurence', models.CharField(max_length=200)),
                ('statuc', models.BooleanField(default=False)),
            ],
        ),
    ]
