# Generated by Django 4.1.6 on 2023-02-07 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("categoria", "0002_alter_categoria_nome"),
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="status",
            field=models.BooleanField(
                default=True, help_text="status do produto", verbose_name="status"
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="categoria do produto",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categoria.categoria",
                verbose_name="categoria",
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="nome",
            field=models.CharField(
                help_text="nome do produto", max_length=100, verbose_name="nome"
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="preco",
            field=models.FloatField(help_text="preço do produto", verbose_name="preço"),
        ),
    ]
