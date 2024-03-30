from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vacancy/", include("vacancy.urls")),
    path("aes/", include("aes.urls")),
]
