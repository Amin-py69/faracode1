# Generated by Django 4.2.7 on 2023-11-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
    ]