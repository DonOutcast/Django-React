# Generated by Django 5.0.2 on 2024-03-04 19:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distribution', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('SEND', 'Отправлено'), ('DRAFT', 'Черновик')], default='DRAFT', max_length=20)),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='distribution.distribution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
