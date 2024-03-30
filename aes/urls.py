from django.urls import path
from . import views

urlpatterns = [
    path("", views.encrypt_data, name="encrypt_data"),
    path("decrypt/", views.decrypt_data, name="decrypt_data"),
]
