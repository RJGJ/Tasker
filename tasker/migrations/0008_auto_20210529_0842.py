# Generated by Django 3.2 on 2021-05-29 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0007_alter_task_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasker.departmentfile'),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('TODO', 'To do'), ('DOING', 'In Progress'), ('DONE', 'Done')], default='TODO', max_length=16),
        ),
    ]
