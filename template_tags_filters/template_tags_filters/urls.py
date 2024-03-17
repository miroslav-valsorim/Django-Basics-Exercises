"""
MAIN URLS
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filters/', include('template_tags_filters.simple.urls')),
]
