# Generated by Django 4.2.6 on 2023-11-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_user_alter_project_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_completed']},
        ),
    ]