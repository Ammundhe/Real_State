from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="HomePage"),
    path("property", views.Property.as_view(), name="Property"),
    path("property/<int:propertyId>", views.Property.as_view(), name="Property")
]