# Generated by Django 3.1.7 on 2021-03-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_delete_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('pnumber', models.CharField(max_length=20)),
                ('uemail', models.EmailField(max_length=20)),
                ('pword', models.CharField(max_length=20)),
            ],
        ),
    ]
