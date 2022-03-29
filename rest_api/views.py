from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.settings import api_settings
from rest_api.serializers import signup_serializer, listing_serializer, realtor_serializer, inquery_serializer
from django.contrib.auth.models import User
from listing.models import listing
from realtor.models import realtor
from inquery.models import inquery


class LoginPage(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class signup(ModelViewSet):
    serializer_class=signup_serializer
    queryset= User.objects.filter(is_superuser=False, is_staff=False)

class Property(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=[IsAuthenticated]
    filter_backends=[filters.SearchFilter, filters.OrderingFilter]
    search_fields=("title",)
    ordering_fields=["id"]
    http_method_names=["get"]
    serializer_class=listing_serializer
    queryset=listing.objects.all()

class Agents(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=[IsAuthenticated]
    serializer_class=realtor_serializer
    queryset=realtor.objects.all()

class Contact(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=[IsAuthenticated]
    serializer_class=inquery_serializer
    queryset=inquery.objects.all()