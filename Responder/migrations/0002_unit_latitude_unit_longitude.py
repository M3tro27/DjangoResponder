# Generated by Django 4.2.11 on 2024-04-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Responder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='latitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='longitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
