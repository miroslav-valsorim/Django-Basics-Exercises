from django.urls import path, include

from exam_prep_one.albums.views import album_add, album_details, album_edit, album_delete

urlpatterns = (
    path('add/', album_add, name='album-add'),
    path('<int:pk>/', include([
        path('details/', album_details, name='album_details'),
        path('edit/', album_edit, name='album_edit'),
        path('delete/', album_delete, name='album_delete'),
        ],
    )),
)
