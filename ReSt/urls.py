from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('api/', include('api_basic.urls')),
    #path('listings/', include('listings.urls')),
    #path('pages/', include('pages.urls')),
    path('api/realty/', include('realty.urls')),
    path('api/realtor/', include('realtors.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
