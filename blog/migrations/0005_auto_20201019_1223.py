# Generated by Django 3.0.7 on 2020-10-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201019_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/static/blog/images/default.png', upload_to='images'),
        ),
    ]
