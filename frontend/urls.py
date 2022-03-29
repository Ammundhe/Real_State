from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="HomePage"),
    path("property", views.Property.as_view(), name="Property"),
    path("property/<int:propertyId>", views.Property.as_view(), name="Property"),
    path("contact-us", views.Contact.as_view(), name="Contact"),
    path("agents", views.Agents.as_view(), name="Agents")
]