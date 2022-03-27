from django.contrib import admin
from realtor.models import realtor


class realtorAdmin (admin.ModelAdmin):
    list_display=("name", "email", "phoneNumber")
    list_filter=["name"]
    search_fields=["name"]

admin.site.register(realtor, realtorAdmin)


