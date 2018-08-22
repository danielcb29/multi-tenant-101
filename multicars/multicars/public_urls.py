from django.urls import include, path
from companies.views import PublicCompanyView

urlpatterns = [
    path('', PublicCompanyView.as_view())
]