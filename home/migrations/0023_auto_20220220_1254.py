# Generated by Django 2.2.12 on 2022-02-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20220220_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('1', 'I do not know now'), ('2', 'Φυσική Καταστροφή - πλημμύρες'), ('3', 'Φυσική Καταστροφή - φωτιές'), ('4', 'Φυσική Καταστροφή - σεισμός'), ('5', 'Φυσική Καταστροφή - Καταστροφή Δημόσιας Περιουσίας'), ('6', 'Φυσική Καταστροφή - Ρύπανση'), ('7', 'Δολιοφθορές - Ρύπανση'), ('8', 'Δολιοφθορές - Καταστροφή Δημόσιας Περιουσίας'), ('9', 'Δολιοφθορές - Ξυλοδαρμός'), ('10', 'Δολιοφθορές - Κλοπή'), ('11', 'Δολιοφθορές - Εμπρισμός')], default='Δεν γνωρίζω', max_length=50),
        ),
    ]
