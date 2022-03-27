from pyexpat import model
from django.contrib import admin
from listing.models import listing, listing_images

class listing_imagesAdmin(admin.TabularInline):
    model=listing_images
    extra=1
    classes=("collapse",)


class listingAdmin(admin.ModelAdmin):
    list_display=["realtor", 'title', 'price', 'state','city','created']
    list_filter=["state"]
    search_fields=["title", "price", "state", "city"]
    inlines=[listing_imagesAdmin]

admin.site.register(listing, listingAdmin)