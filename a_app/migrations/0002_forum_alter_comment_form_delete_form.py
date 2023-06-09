# Generated by Django 4.1.6 on 2023-04-17 08:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('category', models.CharField(choices=[('Q', 'Question'), ('I', 'Information')], max_length=1)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('istifadeci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_comments', to='a_app.forum'),
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
