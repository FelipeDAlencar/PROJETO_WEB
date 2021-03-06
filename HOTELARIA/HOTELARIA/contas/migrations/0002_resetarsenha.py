# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-14 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetarSenha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('criada_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('confirmacao', models.BooleanField(default=False, verbose_name='confirmado?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resetar', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Nova Senha',
                'verbose_name_plural': 'Novas senhas',
                'ordering': ['-criada_em'],
            },
        ),
    ]
