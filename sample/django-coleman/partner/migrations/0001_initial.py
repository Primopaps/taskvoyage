# Generated by Django 3.2.12 on 2022-02-11 03:21

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
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='website')),
                ('is_company', models.BooleanField(default=False, verbose_name='is a company')),
                ('phone', models.CharField(blank=True, max_length=40, null=True, verbose_name='phone')),
                ('mobile', models.CharField(blank=True, max_length=40, null=True, verbose_name='mobile')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='address')),
                ('comment', models.TextField(blank=True, max_length=2000, null=True, verbose_name='notes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ['name'],
            },
        ),
    ]
