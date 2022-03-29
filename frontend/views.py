from webbrowser import get
from django.shortcuts import redirect, render
from django.views import View
from listing.models import listing
from realtor.models import realtor
from inquery.models import inquery
from .modelsForms import inqueryForm, contactform

class HomePage(View):
    template_name="HomePage.html"
    def get(self, request):
        house=listing.objects.all().order_by('-id')[:3]
        agents=realtor.objects.all()
        context={
            "house":house,
            "agents":agents,
        }
        return render(request,self.template_name, context)

class Property(View):
    template_name="property.html"
    form_class=inqueryForm

    def get(self, request, propertyId=None):
        if propertyId:
            singleproperty=listing.objects.get(id=propertyId)
            form=self.form_class()

            context={
                "singleproperty":singleproperty,
                "form":form,
                "propertyId":propertyId,
            }
            return render(request, "propertyDetails.html", context)
        if request.GET.get("search"):
            city=request.GET.get("search")
            properties=listing.objects.filter(city__icontains=city)
            print(properties)
            context={
                "properties":properties
            }

            return render(request, self.template_name, context)
        properties=listing.objects.all()
        context={
            "properties":properties
        }

        return render(request, self.template_name, context)
    
    def post(self, request, propertyId=None):
        singleProperty=listing.objects.get(id=propertyId)
        form=self.form_class(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phoneNumber=form.cleaned_data.get("phoneNumber")
            inquery.objects.create(
                listing_id=propertyId,
                realtor_id=singleProperty.realtor_id,
                name=name,
                email=email,
                phoneNumber=phoneNumber
            )
            return redirect("Property", propertyId=propertyId)
        return redirect("Property", propertyId=propertyId)
        
class Contact(View):
    template_name="contact.html"
    form_class=contactform
    def get(self, request):
        form=self.form_class()
        context={
            "form":form,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Contact")

class Agents(View):
    template_name="agents.html"

    def get(self, request):
        agent=realtor.objects.all()
        context={
            "agent":agent
        }
        return render(request, self.template_name, context)