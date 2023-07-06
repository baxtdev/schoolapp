# Generated by Django 4.0.4 on 2022-06-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220609_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'verbose_name_plural': 'а, б'},
        ),
        migrations.AlterField(
            model_name='abc',
            name='letter_class',
            field=models.CharField(choices=[('A', 'А'), ('Б', 'Б')], default=None, max_length=10, null=True),
        ),
    ]
