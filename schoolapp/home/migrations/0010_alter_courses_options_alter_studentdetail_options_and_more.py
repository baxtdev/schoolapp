# Generated by Django 4.0.5 on 2022-06-08 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_std_courses_number_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name_plural': 'Класстар'},
        ),
        migrations.AlterModelOptions(
            name='studentdetail',
            options={'verbose_name_plural': 'Окуучулар'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name_plural': 'Мугалимдер'},
        ),
    ]
