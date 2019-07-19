# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-15 05:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='hotel/imagens', verbose_name='Imagem')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-mail')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_hotel', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Hotél',
                'verbose_name_plural': 'Hotéis',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='hotel',
            unique_together=set([('user',)]),
        ),
    ]