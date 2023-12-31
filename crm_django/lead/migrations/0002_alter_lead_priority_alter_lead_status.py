# Generated by Django 4.2.2 on 2023-08-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('high', 'High'), ('medium', 'medium')], default='low', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('won', 'Won'), (' contacted', 'Contacted'), ('new', 'New'), ('lost', 'Lost'), ('inprogress', 'In progress')], default='new', max_length=25),
        ),
    ]
