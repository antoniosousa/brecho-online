from django.db import models


class Categoria(models.Model):
    nome = models.CharField("nome", help_text="nome da categoria", max_length=100)

    class Meta:
        db_table = "categoria"

    def __str__(self):
        return f"{self.nome}"
