# Generated by Django 3.2.9 on 2022-07-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizcategory',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name_plural': 'Question'},
        ),
    ]
