# Generated by Django 4.2.7 on 2023-11-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='instagram',
            field=models.CharField(default='in.me2222', max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='telegram',
            field=models.CharField(default='wa.me2222', max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='whatsapp',
            field=models.CharField(default='te.me2222', max_length=100),
        ),
    ]
