# Generated by Django 2.2.28 on 2022-08-21 11:21

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
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название')),
                ('text', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
