# Generated by Django 4.2.1 on 2023-06-11 12:18

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_notes', models.CharField(default='None', max_length=500)),
                ('p_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date', models.DateField(default=None, null=True)),
                ('project_link', models.URLField(null=True)),
                ('downloaded', models.ManyToManyField(blank=True, default=None, related_name='downloaded', to=settings.AUTH_USER_MODEL)),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('p_creator', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_creator', to=settings.AUTH_USER_MODEL)),
                ('tagged', models.ManyToManyField(blank=True, default=None, related_name='tagged', to=settings.AUTH_USER_MODEL)),
                ('viewed', models.ManyToManyField(blank=True, default=None, related_name='viewed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Viewers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pv_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
                ('viewer', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='None', max_length=100)),
                ('p_tag_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
                ('tagger', models.ForeignKey(default=None, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(default='None', max_length=100)),
                ('father', models.CharField(default='None', max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(default='None', max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('email', models.EmailField(default='None', max_length=254)),
                ('friend', models.ManyToManyField(blank=True, default=None, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('proj_created', models.ManyToManyField(blank=True, default=None, related_name='proj_created', to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Pcomments',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('comment', models.CharField(default='None', max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.pcomments')),
                ('pname', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
                ('username', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lovers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('lover', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('p_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Gcomments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcomment', models.CharField(default='None', max_length=1000)),
                ('date', models.DateField()),
                ('username', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_n', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_n', to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorby', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Downloaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloader', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pd_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
            ],
        ),
    ]
