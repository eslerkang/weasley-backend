# Generated by Django 3.2.9 on 2021-11-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.PositiveIntegerField(),
        ),
    ]
