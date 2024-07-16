# Generated by Django 5.0 on 2024-06-24 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField(default='')),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
                ('prop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.property')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
