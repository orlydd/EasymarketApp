# Generated by Django 3.0.2 on 2020-02-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
    ]