from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cars.models import Car

# Create your views here.
class CompanyInformationView(ListView):
    template_name = 'companies/tenant.html'
    model = Car

class PublicCompanyView(TemplateView):
    template_name = 'companies/public.html'
