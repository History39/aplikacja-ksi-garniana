# Generated by Django 4.2 on 2023-04-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_bookdetail_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='description',
            field=models.TextField(),
        ),
    ]
