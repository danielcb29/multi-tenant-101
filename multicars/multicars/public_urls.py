from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from companies.views import PublicCompanyView

urlpatterns = [
    path('', PublicCompanyView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)