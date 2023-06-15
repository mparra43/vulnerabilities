# Generated by Django 4.2.2 on 2023-06-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Todas', 'Todas'), ('Fixeadas', 'Fixeadas')], default='Todas', max_length=20)),
                ('severity', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], default='LOW', max_length=20)),
            ],
        ),
    ]