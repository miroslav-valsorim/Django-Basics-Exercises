from django.urls import path

from forms_first_excercise.normal_form.views import normal_form

urlpatterns = (
    path('', normal_form, name='normal_form'),
)
