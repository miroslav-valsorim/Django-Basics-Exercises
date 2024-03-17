from django.urls import path

from template_tags_filters.simple.views import index

urlpatterns = (
    path('', index, name='index'),
)
