# Generated by Django 4.0.4 on 2022-05-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]