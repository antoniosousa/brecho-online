# Generated by Django 4.1.6 on 2023-02-07 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0002_produto_status_alter_produto_categoria_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(upload_to="templates/produto/imagens"),
        ),
    ]
