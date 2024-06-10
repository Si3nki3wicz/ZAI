# Generated by Django 5.0.6 on 2024-06-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0010_alter_extrainfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'Dramat'), (2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi')], null=True),
        ),
    ]
