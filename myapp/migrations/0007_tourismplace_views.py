# Generated by Django 5.1.1 on 2024-09-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_tourismplace_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourismplace',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
