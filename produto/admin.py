from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from estoque.models import Estoque

from .models import Produto


class ProdutoFilterStatus(SimpleListFilter):
    title = "Status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return (
            ("ativo", "Ativo para exibir"),
            ("inativo", "Inativo para exibir"),
        )

    def queryset(self, request, queryset):
        if self.value() == "ativo":
            return queryset.filter(status=True)
        if self.value() == "inativo":
            return queryset.filter(status=False)
        return queryset


def exibir_produtos_selecionados(modeladmin, request, queryset):
    queryset.update(status=True)


def nao_exibir_produtos_selecionados(modeladmin, request, queryset):
    queryset.update(status=False)


class EstoqueInline(admin.StackedInline):
    model = Estoque


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "categoria", "status")
    inlines = [EstoqueInline]
    list_filter = [ProdutoFilterStatus]
    actions = [
        exibir_produtos_selecionados,
        nao_exibir_produtos_selecionados,
    ]


admin.site.register(Produto, ProdutoAdmin)
