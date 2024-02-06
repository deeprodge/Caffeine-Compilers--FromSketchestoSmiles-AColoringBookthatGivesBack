# Generated by Django 3.2 on 2024-01-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240129_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='cover_url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='drawings',
            field=models.ManyToManyField(null=True, to='api.Drawings'),
        ),
    ]