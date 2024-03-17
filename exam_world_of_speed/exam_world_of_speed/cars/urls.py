from django.urls import path, include

from exam_world_of_speed.cars.views import car_catalogue, car_create, car_edit, car_details, car_delete

urlpatterns = (
    path('catalogue/', car_catalogue, name='car_catalogue'),
    path('create/', car_create, name='car_create'),
    path('<id>/', include([
        path('edit/', car_edit, name='car_edit'),
        path('details/', car_details, name='car_details'),
        path('delete/', car_delete, name='car_delete'),
    ]),),
)