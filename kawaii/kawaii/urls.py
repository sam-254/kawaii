"""kawaii URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'))
]

handler404 = 'news.views.error_404_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)