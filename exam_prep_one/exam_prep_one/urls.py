
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from exam_prep_one import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_prep_one.mainpage.urls')),
    path('album/', include('exam_prep_one.albums.urls')),
    path('profile/', include('exam_prep_one.profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
