from django.db import models
from realtor.models import realtor

class listing(models.Model):
    property_chioces=(
        ("sale", "sale"),
        ("rent", "rent")
    )
    realtor=models.ForeignKey(realtor, on_delete=models.CASCADE, related_name="realtor")
    title=models.CharField(max_length=150)
    description=models.TextField()
    city=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    state=models.CharField(max_length=155)
    cover_image=models.ImageField()
    price=models.DecimalField( max_digits=12, decimal_places=2)
    bedroom=models.IntegerField()
    bathroom=models.IntegerField()
    Area=models.IntegerField(null=True, blank=True)
    property_status=models.CharField(max_length=255, choices=property_chioces, default="sale", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class listing_images(models.Model):
    listing=models.ForeignKey(listing, on_delete=models.CASCADE, related_name="listingImages")
    image=models.ImageField()

    def __str__(self) -> str:
        return str(self.listing)