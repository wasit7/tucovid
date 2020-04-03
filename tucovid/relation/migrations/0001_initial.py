# Generated by Django 3.0.4 on 2020-04-03 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('01', 'สามี/ภรรยา'), ('02', 'เพื่อนร่วมงาน/เพื่อนร่วมชั้น'), ('03', ' เพื่อนสนิท/คนรัก'), ('04', 'เพื่อนร่วมห้อง')], max_length=2)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relation_creator', to=settings.AUTH_USER_MODEL)),
                ('persons', models.ManyToManyField(related_name='relationship', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('location', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_creator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participant', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
