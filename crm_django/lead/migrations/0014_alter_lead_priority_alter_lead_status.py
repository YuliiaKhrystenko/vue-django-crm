# Generated by Django 4.2.3 on 2023-08-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0013_alter_lead_priority_alter_lead_status'),
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
            field=models.CharField(choices=[('lost', 'Lost'), ('won', 'Won'), ('inprogress', 'In progress'), ('new', 'New'), (' contacted', 'Contacted')], default='new', max_length=25),
        ),
    ]
