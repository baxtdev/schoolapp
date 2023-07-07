# Generated by Django 4.1.6 on 2023-07-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Арыз',
                'verbose_name_plural': 'Арыздар',
            },
        ),
        migrations.CreateModel(
            name='Schole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связы',
            },
        ),
    ]