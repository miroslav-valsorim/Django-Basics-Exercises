from django.urls import path

from exam_prep_two.mainpage.views import main_page, dashboard

urlpatterns = (
    path('', main_page, name='main_page'),
    path('dashboard/', dashboard, name='dashboard')
)