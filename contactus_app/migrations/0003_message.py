# Generated by Django 4.2.7 on 2023-11-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0002_contactus_instagram_contactus_telegram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=150)),
                ('body', models.TextField()),
            ],
        ),
    ]
