from django.urls import path

from .views import categoria, lista, subtrai_estoque

app_name = "produto"
urlpatterns = [
    path("lista/", lista, name="lista"),
    path("categoria/<int:categoria_id>/", categoria, name="categoria"),
    path("tenho-interesse/<int:produto_id>/", subtrai_estoque, name="subtrai_estoque"),
]
