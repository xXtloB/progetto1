# Generated by Django 3.1.1 on 2020-12-09 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='genere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.genere'),
        ),
    ]