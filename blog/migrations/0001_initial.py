# Generated by Django 3.0.7 on 2020-11-09 08:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20201104_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('blog', models.TextField(max_length=2000)),
                ('date', models.DateField(default=datetime.datetime(2020, 11, 9, 14, 3, 42, 31869))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserModel')),
            ],
        ),
    ]
