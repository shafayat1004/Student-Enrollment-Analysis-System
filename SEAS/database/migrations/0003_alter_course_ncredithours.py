# Generated by Django 3.2.7 on 2021-11-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_course_department_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='nCreditHours',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
