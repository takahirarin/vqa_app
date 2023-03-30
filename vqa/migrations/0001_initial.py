# Generated by Django 3.2.8 on 2023-02-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.CharField(default='', max_length=200)),
                ('answer', models.CharField(default='', max_length=200)),
            ],
        ),
    ]