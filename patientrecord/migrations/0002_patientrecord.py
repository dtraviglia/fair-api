# Generated by Django 2.1.7 on 2019-04-03 19:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patientrecord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('date_of_birth', models.DateField(blank=True)),
            ],
        ),
    ]