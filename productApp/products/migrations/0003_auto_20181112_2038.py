# Generated by Django 2.1.3 on 2018-11-12 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181110_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description_text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_num',
            new_name='price',
        ),
    ]
