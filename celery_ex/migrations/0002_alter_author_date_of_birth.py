# Generated by Django 4.1.7 on 2023-04-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_ex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
    ]