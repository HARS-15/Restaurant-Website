# Generated by Django 5.0.2 on 2024-05-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurent', '0002_neutral'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('menu_category', models.CharField(max_length=20)),
                ('item_type', models.CharField(max_length=2)),
            ],
        ),
    ]