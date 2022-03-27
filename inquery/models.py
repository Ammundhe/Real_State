import email
from django.db import models
from realtor.models import realtor
from listing.models import listing

class inquery(models.Model):
    listing=models.ForeignKey(listing, on_delete=models.CASCADE)
    realtor=models.ForeignKey(realtor, on_delete=models.CASCADE)
    name=models.CharField(max_length=155)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)

    def __str__(self) -> str:
        return str(self.name)
