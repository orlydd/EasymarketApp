# Generated by Django 3.0.2 on 2020-03-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_aplicacion', '0007_auto_20200305_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
