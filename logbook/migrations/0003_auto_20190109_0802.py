# Generated by Django 2.1.4 on 2019-01-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('logbook', '0002_auto_20190103_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='plan',
            field=models.TextField(default='', help_text='Enter the patients plan here', max_length=1000),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='notes',
            field=models.TextField(help_text='Enter a description of the consultation. Do not include the plan.',
                                   max_length=1000),
        ),
    ]
