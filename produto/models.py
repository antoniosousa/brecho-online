from django.db import models
from PIL import Image

from categoria.models import Categoria
from estoque.models import Estoque


class Produto(models.Model):
    nome = models.CharField("nome", help_text="nome do produto", max_length=100)
    preco = models.FloatField("preço", help_text="preço do produto")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        verbose_name="categoria",
        help_text="categoria do produto",
    )
    imagem = models.ImageField(upload_to="templates/produto/imagens")
    status = models.BooleanField(
        "status", help_text="status do produto para exibição", default=True
    )

    class Meta:
        db_table = "produto"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.imagem.path)
        size = (300, 300)
        img = img.resize(size, resample=Image.ANTIALIAS)
        img.save(self.imagem.path)

    def __str__(self):
        return f"{self.id} - {self.nome}"

    @property
    def estoque(self):
        return Estoque.objects.filter(produto=self).first()

    def set_status(self):
        if self.status is True:
            if not self.estoque.tem_estoque:
                self.status = False
                self.save()
