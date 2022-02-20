# Generated by Django 2.2.12 on 2022-02-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_blogpost_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('1', 'I do not know now'), ('2', 'Φυσική Καταστροφή - πλημμύρες'), ('3', 'Φυσική Καταστροφή - φωτιές'), ('4', 'Φυσική Καταστροφή - σεισμός'), ('5', 'Φυσική Καταστροφή - Καταστροφή Δημόσιας Περιουσίας'), ('6', 'Φυσική Καταστροφή - Ρύπανση'), ('7', 'Δολιοφθορές - Ρύπανση'), ('8', 'Δολιοφθορές - Καταστροφή Δημόσιας Περιουσίας'), ('9', 'Δολιοφθορές - Ξυλοδαρμός'), ('10', 'Δολιοφθορές - Κλοπή')], default='Δεν γνωρίζω', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='dhmos',
            field=models.CharField(choices=[('1', 'Παράδειγμα Δήμου1'), ('2', 'Παράδειγμα Δήμου2'), ('3', 'Παράδειγμα Δήμου3'), ('4', 'Παράδειγμα Δήμου4'), ('5', 'Παράδειγμα Δήμου5'), ('6', 'Παράδειγμα Δήμου6'), ('7', 'Παράδειγμα Δήμου7'), ('8', 'Παράδειγμα Δήμου8'), ('9', 'Παράδειγμα Δήμου9'), ('10', 'Παράδειγμα Δήμου10')], default='Παράδειγμα Δήμου1', max_length=50),
        ),
    ]