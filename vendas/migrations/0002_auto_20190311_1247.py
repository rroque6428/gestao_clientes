# Generated by Django 2.0.13 on 2019-03-11 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItensDoPedido',
            new_name='ItemDoPedido',
        ),
    ]