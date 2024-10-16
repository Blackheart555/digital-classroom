# Generated by Django 5.1.1 on 2024-10-05 22:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st', 'First Semester'), ('2nd', 'Second Semester'), ('3rd', 'Third Semester'), ('4th', 'Fourth Semester'), ('5th', 'Fifth Semester'), ('6th', 'Sixth Semester'), ('7th', 'Seventh Semester'), ('8th', 'Eighth Semester')], default='1st', max_length=10)),
                ('file', models.FileField(null=True, upload_to='routines/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routines', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'routines',
            },
        ),
    ]
