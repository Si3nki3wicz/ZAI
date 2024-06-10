# Generated by Django 5.0.6 on 2024-06-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0007_rename_film_extrainfo_filmy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Komedia'), (4, 'Dramat'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi')], null=True),
        ),
    ]
