# Generated by Django 3.0.2 on 2020-02-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
