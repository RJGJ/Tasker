# Generated by Django 3.2 on 2021-04-28 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_alter_submition_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='submition',
            name='goal',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasker.taskitem'),
        ),
    ]