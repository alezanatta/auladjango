# Generated by Django 3.0.5 on 2020-04-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dsc_complemento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nr_endereco',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
