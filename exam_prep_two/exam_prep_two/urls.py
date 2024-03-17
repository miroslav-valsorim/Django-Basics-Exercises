"""
MAIN URLS
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_prep_two.mainpage.urls')),
    path('fruit/', include('exam_prep_two.fruits.urls')),
    path('profile/', include('exam_prep_two.profiles.urls')),
]
