# Generated by Django 2.1.4 on 2019-03-16 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0010_auto_20190316_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='notes',
            field=models.TextField(blank=True, help_text='Enter a description of the procedure', max_length=20000, null=True),
        ),
    ]
