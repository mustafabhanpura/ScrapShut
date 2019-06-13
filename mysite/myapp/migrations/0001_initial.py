# Generated by Django 2.0.1 on 2019-06-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('video', models.FileField(upload_to='videos/')),
                ('stream', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
