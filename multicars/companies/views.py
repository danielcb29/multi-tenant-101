from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CompanyInformationView(TemplateView):
    template_name = 'companies/tenant.html'

class PublicCompanyView(TemplateView):
    template_name = 'companies/public.html'
