# Generated by Django 2.2.4 on 2019-11-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default/default_post_img.jpg', upload_to='posts/img'),
        ),
    ]
