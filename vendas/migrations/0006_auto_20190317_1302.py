# Generated by Django 2.0.13 on 2019-03-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20190311_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar param NFe'), ('persmissao2', 'Descrição permissão'))},
        ),
    ]
