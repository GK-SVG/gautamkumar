# Generated by Django 3.0.6 on 2020-05-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plateform',
            name='org_image',
            field=models.CharField(max_length=265),
        ),
    ]
