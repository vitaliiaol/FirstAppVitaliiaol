# Generated by Django 3.0.2 on 2020-01-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('biography', models.TextField(blank=True)),
                ('date_of_birth', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'bt_author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True)),
                ('pages', models.IntegerField()),
                ('genre', models.CharField(blank=True, max_length=35)),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
            options={
                'db_table': 'bt_book',
            },
        ),
    ]