# Generated by Django 3.2 on 2021-04-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=None),
        ),
    ]