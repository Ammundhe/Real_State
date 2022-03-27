from operator import mod
from pyexpat import model
from turtle import title
from django.db import models
from realtor.models import realtor

class listing(models.Model):
    realtor=models.ForeignKey(realtor, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    state=models.CharField(max_length=155)
    cover_image=models.ImageField()
    price=models.DecimalField( max_digits=12, decimal_places=2)
    betroom=models.IntegerField()
    bathroom=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class listing_images(models.Model):
    listing=models.ForeignKey(listing, on_delete=models.CASCADE)
    image=models.ImageField()

    def __str__(self) -> str:
        return str(self.listing)