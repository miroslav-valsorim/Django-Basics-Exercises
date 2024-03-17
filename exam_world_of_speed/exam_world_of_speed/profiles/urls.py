from django.urls import path

from exam_world_of_speed.profiles.views import create_profile, edit_profile, details_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('details/', details_profile, name='details_profile'),
    path('delete/', delete_profile, name='delete_profile'),
)