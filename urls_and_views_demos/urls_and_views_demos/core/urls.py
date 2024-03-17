from django.urls import path, include

from urls_and_views_demos.core.views import index, index_json

urlpatterns = (
    path("", index),
    path("<int:pk>/", index),
    path("<slug:slug>/", index),
    path("<int:pk>/<slug:slug>", index),
    path("<str:pk>/", index),

    # for JSON
    path('json/', include([
        path("", index_json),
        path("<int:pk>/", index_json),
        path("<slug:slug>/", index_json),
        path("<int:pk>/<slug:slug>", index_json),
        path("<str:pk>/", index_json),
    ]))
)
