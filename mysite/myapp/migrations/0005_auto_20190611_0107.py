# Generated by Django 2.0.1 on 2019-06-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190611_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='image',
            field=models.FileField(upload_to='pic_folder/'),
        ),
    ]
