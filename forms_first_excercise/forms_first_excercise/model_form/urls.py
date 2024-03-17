from django.urls import path

from forms_first_excercise.model_form.views import model_form, update_person

urlpatterns = (
    path('', model_form, name='model_form'),
    path('<int:pk>/', update_person, name='update_person'),
)