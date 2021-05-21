from typing import List
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.urls.resolvers import URLPattern, URLResolver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('tasker.urls')),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
