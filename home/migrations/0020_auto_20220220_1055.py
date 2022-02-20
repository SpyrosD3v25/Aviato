# Generated by Django 2.2.12 on 2022-02-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20220219_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='dhmos',
            field=models.CharField(choices=[('1', 'Παράδειγμα Δήμου1'), ('2', 'Παράδειγμα Δήμου2'), ('2', 'Παράδειγμα Δήμου3'), ('2', 'Παράδειγμα Δήμου4'), ('2', 'Παράδειγμα Δήμου5'), ('2', 'Παράδειγμα Δήμου6'), ('3', 'Παράδειγμα Δήμου7'), ('3', 'Παράδειγμα Δήμου8'), ('3', 'Παράδειγμα Δήμου9'), ('3', 'Παράδειγμα Δήμου10')], default='Παράδειγμα Δήμου1', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('1', 'I do not know now'), ('2', 'Φυσική Καταστροφή - πλημμύρες'), ('2', 'Φυσική Καταστροφή - φωτιές'), ('2', 'Φυσική Καταστροφή - σεισμός'), ('2', 'Φυσική Καταστροφή - Καταστροφή Δημόσιας Περιουσίας'), ('2', 'Φυσική Καταστροφή - Ρύπανση'), ('3', 'Δολιοφθορές - Ρύπανση'), ('3', 'Δολιοφθορές - Καταστροφή Δημόσιας Περιουσίας'), ('3', 'Δολιοφθορές - Ξυλοδαρμός'), ('3', 'Δολιοφθορές - Κλοπή')], default='Δεν γνωρίζω', max_length=50),
        ),
    ]