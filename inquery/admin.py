from django.contrib import admin
from inquery.models import inquery


class inqueryAdmin(admin.ModelAdmin):
    list_display=['realtor', 'listing','name', 'email', 'phoneNumber' ]
    list_filter=['realtor']
    search_fields=['name','listing', 'realtor']


admin.site.register(inquery, inqueryAdmin)
