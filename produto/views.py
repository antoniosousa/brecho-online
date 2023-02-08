from django.conf import settings
from django.shortcuts import redirect, render

from categoria.models import Categoria
from produto.models import Produto


def lista(request):
    categorias = Categoria.objects.all().order_by("nome")
    produtos = Produto.objects.filter(status=True).order_by("-id")
    contexto = {"produtos": produtos, "categorias": categorias}
    return render(request, "produto/index.html", contexto)


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, "produto/index.html", {"produtos": produtos})


def subtrai_estoque(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.estoque.subtrair_um_do_estoque()
    produto.set_status()
    return redirect(
        f"https://api.whatsapp.com/send?phone={settings.TELEFONE_SUPORTE}&text=Olá, tenho interesse no produto: {produto.id} - {produto.nome}"
    )
