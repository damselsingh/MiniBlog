# Generated by Django 3.0.7 on 2020-10-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201019_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images'),
        ),
    ]