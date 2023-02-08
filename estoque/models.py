from django.db import models


class Estoque(models.Model):
    produto = models.OneToOneField(
        "produto.Produto",
        on_delete=models.CASCADE,
        verbose_name="produto",
        help_text="produto",
    )
    quantidade = models.PositiveIntegerField("quantidade", help_text="quantidade")

    class Meta:
        db_table = "estoque"

    def __str__(self):
        return f"{self.quantidade}"

    @property
    def tem_estoque(self):
        return self.quantidade != 0

    def subtrair_um_do_estoque(self):
        if self.tem_estoque:
            self.quantidade -= 1
            self.save()
            return True
        return False
