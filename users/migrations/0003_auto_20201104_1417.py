# Generated by Django 3.0.7 on 2020-11-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201102_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'ordering': ['firstname']},
        ),
        migrations.AddField(
            model_name='usermodel',
            name='pic',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
