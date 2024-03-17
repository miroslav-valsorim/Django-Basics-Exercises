from django.urls import path

from exam_world_of_speed.main.views import index

urlpatterns = (
    path('', index, name='index'),
)