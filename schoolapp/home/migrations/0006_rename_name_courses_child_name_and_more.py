# Generated by Django 4.0.4 on 2022-06-03 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_courses_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='name',
            new_name='child_name',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='student_name',
        ),
        migrations.AddField(
            model_name='courses',
            name='classes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.studentdetail'),
            preserve_default=False,
        ),
    ]
