"""
    URL CONFIGURATION
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from .views import Home

API_V1_ROUTER_ADMIN = DefaultRouter()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="Asociaciones API")),
    path("api/v1/", include("api.urls")),
]


if settings.DEBUG:
    urlpatterns.append(path("", Home.as_view()))

    urlpatterns += static(settings.COV_URL, document_root=settings.COV_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
