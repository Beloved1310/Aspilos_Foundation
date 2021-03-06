# Generated by Django 3.1.7 on 2021-04-11 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project.post')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
