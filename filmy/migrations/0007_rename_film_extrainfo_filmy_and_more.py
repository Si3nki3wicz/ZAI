# Generated by Django 5.0.6 on 2024-06-10 22:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0006_rename_imdb_pkts_film_imdb_points_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrainfo',
            old_name='film',
            new_name='filmy',
        ),
        migrations.RemoveField(
            model_name='extrainfo',
            name='punkty_widzow',
        ),
        migrations.AddField(
            model_name='aktor',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aktorzy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='einfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='film',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filmy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ocena',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oceny', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='filmy',
            field=models.ManyToManyField(blank=True, to='filmy.film'),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'Dramat'), (2, 'Komedia'), (3, 'Sci-fi'), (0, 'Inne'), (1, 'Horror')], null=True),
        ),
        migrations.AlterField(
            model_name='ocena',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmy.film'),
        ),
    ]