# Generated by Django 2.2.1 on 2019-05-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ranking', models.CharField(blank=True, choices=[('1', 'Terrible'), ('2', 'Bad'), ('3', 'Average'), ('4', 'Good'), ('5', 'Excellent')], max_length=3, null=True)),
            ],
        ),
    ]