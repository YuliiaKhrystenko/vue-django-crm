# Generated by Django 4.2.2 on 2023-08-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0015_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'medium'), ('low', 'Low')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'New'), (' contacted', 'Contacted'), ('lost', 'Lost'), ('inprogress', 'In progress'), ('won', 'Won')], default='new', max_length=25),
        ),
    ]
