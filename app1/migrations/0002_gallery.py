# Generated by Django 3.2.9 on 2022-01-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='')),
                ('Name', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('Model', models.IntegerField()),
                ('Details', models.CharField(max_length=100)),
            ],
        ),
    ]
