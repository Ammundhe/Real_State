from django import views
from django.urls import path, include
from django.db import router
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register("property", views.Property)
router.register("signup", views.signup)
router.register("agents", views.Agents)
router.register("contact", views.Contact)

urlpatterns = [
    path("login", views.LoginPage.as_view()),
    path("", include(router.urls))
]
