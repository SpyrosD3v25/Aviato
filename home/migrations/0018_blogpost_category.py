# Generated by Django 2.2.12 on 2022-02-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.NullBooleanField(),
        ),
    ]