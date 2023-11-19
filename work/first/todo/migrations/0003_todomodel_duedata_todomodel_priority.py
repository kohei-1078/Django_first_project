# Generated by Django 4.2.6 on 2023-11-04 10:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todomodel_test_alter_todomodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedata',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], default='danger', max_length=50),
            preserve_default=False,
        ),
    ]
