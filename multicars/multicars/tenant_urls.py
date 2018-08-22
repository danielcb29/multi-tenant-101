from django.urls import include, path
from companies.views import CompanyInformationView

urlpatterns = [
    path('', CompanyInformationView.as_view())
]
