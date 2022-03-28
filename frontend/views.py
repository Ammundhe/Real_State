from django.shortcuts import render
from django.views import View
from listing.models import listing
from realtor.models import realtor

class HomePage(View):
    template_name="HomePage.html"

    def get(self, request):
        house=listing.objects.all().order_by('-id')[:3]
        agents=realtor.objects.all()
        context={
            "house":house,
            "agents":agents
        }
        return render(request,self.template_name, context)

class Property(View):
    template_name="property.html"

    def get(self, request, propertyId=None):
        if propertyId:
            singleproperty=listing.objects.get(id=propertyId)
            context={
                "singleproperty":singleproperty
            }
            return render(request, "propertyDetails.html", context)
        properties=listing.objects.all()
        context={
            "properties":properties
        }

        return render(request, self.template_name, context)