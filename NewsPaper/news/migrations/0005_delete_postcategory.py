# Generated by Django 4.0.3 on 2022-04-14 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_post_post_to_category_rel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]