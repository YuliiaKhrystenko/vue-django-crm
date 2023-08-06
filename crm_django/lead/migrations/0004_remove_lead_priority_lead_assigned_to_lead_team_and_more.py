# Generated by Django 4.2.2 on 2023-08-03 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0003_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='priority',
        ),
        migrations.AddField(
            model_name='lead',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedleads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('inprogress', 'In progress'), ('won', 'Won'), (' contacted', 'Contacted'), ('lost', 'Lost'), ('new', 'New')], default='new', max_length=25),
        ),
    ]
