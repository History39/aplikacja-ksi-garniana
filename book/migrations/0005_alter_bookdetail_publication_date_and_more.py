# Generated by Django 4.2 on 2023-04-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_bookdetail_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookmain',
            name='title',
            field=models.TextField(max_length=400),
        ),
    ]
