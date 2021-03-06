# Generated by Django 3.2.7 on 2021-09-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_alter_slider_button_navigate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=255)),
                ('insta_link', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
