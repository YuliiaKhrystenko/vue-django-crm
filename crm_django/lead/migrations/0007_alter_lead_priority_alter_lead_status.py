# Generated by Django 4.2.2 on 2023-08-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_lead_priority_alter_lead_email_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'medium')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('inprogress', 'In progress'), (' contacted', 'Contacted'), ('lost', 'Lost'), ('new', 'New'), ('won', 'Won')], default='new', max_length=25),
        ),
    ]
