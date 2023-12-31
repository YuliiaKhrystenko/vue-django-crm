# Generated by Django 4.2.3 on 2023-08-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0011_alter_lead_priority_alter_lead_status'),
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
            field=models.CharField(choices=[('new', 'New'), ('lost', 'Lost'), ('inprogress', 'In progress'), ('won', 'Won'), (' contacted', 'Contacted')], default='new', max_length=25),
        ),
    ]
