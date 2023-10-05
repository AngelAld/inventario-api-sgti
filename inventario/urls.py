from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaView, AreaView, MarcaView, ItemView
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()

router.register(r"categorias", CategoriaView, "categorias")
router.register(r"areas", AreaView, "areas")
router.register(r"marcas", MarcaView, "marcas")
router.register(r"items", ItemView, "tems")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="APIS DE INVENTARIO")),
]