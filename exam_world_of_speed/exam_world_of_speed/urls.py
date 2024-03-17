"""
MAIN URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_world_of_speed.main.urls')),
    path('car/', include('exam_world_of_speed.cars.urls')),
    path('profile/', include('exam_world_of_speed.profiles.urls')),
]
