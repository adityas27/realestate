# Generated by Django 5.0 on 2024-06-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_rename_contact_contactform_ph_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
