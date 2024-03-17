
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('normalform/', include('forms_first_excercise.normal_form.urls')),
    path('modelform/', include('forms_first_excercise.model_form.urls')),
]
