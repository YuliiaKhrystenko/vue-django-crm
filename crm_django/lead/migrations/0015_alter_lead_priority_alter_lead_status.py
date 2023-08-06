# Generated by Django 4.2.3 on 2023-08-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0014_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'medium'), ('low', 'Low'), ('high', 'High')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[(' contacted', 'Contacted'), ('inprogress', 'In progress'), ('new', 'New'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=25),
        ),
    ]
