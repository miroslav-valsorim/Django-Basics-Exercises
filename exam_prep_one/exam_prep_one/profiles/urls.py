from django.urls import path

from exam_prep_one.profiles.views import profile_details, profile_delete

urlpatterns = (
    path('details/', profile_details, name='profile_details'),
    path('delete/', profile_delete, name='profile_delete'),
)
