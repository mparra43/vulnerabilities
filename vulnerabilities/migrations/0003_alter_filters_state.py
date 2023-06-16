# Generated by Django 4.2.2 on 2023-06-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0002_alter_metrics_base_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filters',
            name='state',
            field=models.CharField(choices=[('Todas', 'Todas'), ('Fixeada', 'Fixeada'), ('Publicadas', 'Publicadas')], default='Todas', max_length=20),
        ),
    ]
