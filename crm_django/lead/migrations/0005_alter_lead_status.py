# Generated by Django 4.2.2 on 2023-08-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_remove_lead_priority_lead_assigned_to_lead_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('lost', 'Lost'), ('won', 'Won'), ('inprogress', 'In progress'), (' contacted', 'Contacted'), ('new', 'New')], default='new', max_length=25),
        ),
    ]
