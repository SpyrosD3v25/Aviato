# Generated by Django 2.2.12 on 2022-02-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.NullBooleanField(choices=[(None, 'I do not know now'), (True, 'Φυσικη Καταστροφη'), (False, 'Εγκληματικοτητα')]),
        ),
    ]