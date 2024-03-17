from django.urls import path, include

from exam_prep_two.fruits.views import create_fruit, details_fruit, edit_fruit, delete_fruit

urlpatterns = (
    path('create/', create_fruit, name='create_fruit'),
    path('<fruitId>/', include([
        path('details/', details_fruit, name='details_fruit'),
        path('edit/', edit_fruit, name='edit_fruit'),
        path('delete/', delete_fruit, name='delete_fruit'),
    ]),
         ),
)
