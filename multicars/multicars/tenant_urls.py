from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from companies.views import CompanyInformationView
from companies.views import PublicCompanyView

urlpatterns = [
    path('', CompanyInformationView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
