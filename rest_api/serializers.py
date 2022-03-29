from rest_framework import serializers
from django.contrib.auth.models import User
from listing.models import listing
from realtor.models import realtor
from inquery.models import inquery

class signup_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "password", "first_name", "last_name", "email"]
        extra_kwargs={
            "password":{"write_only":True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def Update(self, valiadated_data, instance):
        instance.username=valiadated_data.get("username", instance.username)
        instance.first_name=valiadated_data.get("first_name", instance.first_name)
        instance.last_name=valiadated_data.get("last_name", instance.last_name)
        instance.email=valiadated_data.get("email", instance.email)
        instance.set_password=valiadated_data.get("password", instance.set_password)
        instance.save()
        return instance

class listing_serializer(serializers.ModelSerializer):
    class Meta:
        model=listing
        fields="__all__"
    
class realtor_serializer(serializers.ModelSerializer):
    class Meta:
        model=realtor
        fields="__all__"

class inquery_serializer(serializers.ModelSerializer):
    class Meta:
        model=inquery
        fields="__all__"