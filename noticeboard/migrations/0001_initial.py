# Generated by Django 3.2.5 on 2022-09-26 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.CharField(max_length=2000)),
                ('writeDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('writeID', models.CharField(max_length=50)),
            ],
        ),
    ]
