# Generated by Django 3.2 on 2021-05-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0006_alter_departmentfile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('TODO', 'todo'), ('DOING', 'doing'), ('DONE', 'done')], default='TODO', max_length=16),
        ),
    ]
