# Generated by Django 2.1.4 on 2019-03-16 06:52

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0011_auto_20190316_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter a description of the consultation.', max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter a description of the procedure', max_length=20000, null=True),
        ),
    ]