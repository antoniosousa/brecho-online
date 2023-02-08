from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models import F

from .models import Estoque


def acrescentar_uma_unidade_no_estoque_dos_produtos_selecionados(
    modeladmin, request, queryset
):
    queryset.update(quantidade=F("quantidade") + 1)


def zerar_o_estoque_dos_produtos_selecionados(modeladmin, request, queryset):
    queryset.update(quantidade=0)


class EstoqueFilter(SimpleListFilter):
    title = "Estoque"
    parameter_name = "quantidade"

    def lookups(self, request, model_admin):
        return (
            ("zerado", "Produtos sem estoque"),
            ("positivo", "Produtos com estoque"),
        )

    def queryset(self, request, queryset):
        if self.value() == "zerado":
            return queryset.filter(quantidade=0)
        if self.value() == "positivo":
            return queryset.filter(quantidade__gt=0)
        return queryset


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("quantidade", "produto")
    actions = [
        acrescentar_uma_unidade_no_estoque_dos_produtos_selecionados,
        zerar_o_estoque_dos_produtos_selecionados,
    ]
    list_filter = [EstoqueFilter]


admin.site.register(Estoque, EstoqueAdmin)
