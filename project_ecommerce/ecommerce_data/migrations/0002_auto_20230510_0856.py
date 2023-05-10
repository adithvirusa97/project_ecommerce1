# Generated by Django 3.0 on 2023-05-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='catimage',
            field=models.ImageField(default=1, upload_to='categories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategories',
            name='category_description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subcategories',
            name='subcatimage',
            field=models.ImageField(blank=True, null=True, upload_to='subcategories'),
        ),
    ]