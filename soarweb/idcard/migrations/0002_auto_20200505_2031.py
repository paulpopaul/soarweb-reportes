# Generated by Django 3.0.5 on 2020-05-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='theme',
            field=models.CharField(choices=[('Light', 'Light'), ('Blue', 'Blue'), ('Green', 'Green'), ('Dark', 'Dark')], default='Light', max_length=20),
        ),
    ]
