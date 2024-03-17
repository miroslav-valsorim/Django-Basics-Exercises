from django.urls import path

from urls_and_views_demos.departments.views import index2, index, department_details, department_details_by_name

urlpatterns = (
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),
    path("<int:pk>/", department_details),
    path("<str:name>/", department_details_by_name),
)