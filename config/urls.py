from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editora", EditoraViewSet)
router.register(r"autor", AutorViewSet)
router.register(r"livro", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]