from django.urls import path

from app_1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('compute', views.compute, name="compute"),
    path('simple_upload', views.simple_upload, name="simple_upload"),
    path('table_show', views.table_show, name="table_show"),
    path('ajax1', views.ajax1, name="ajax1"),
    path('compute2', views.compute2, name="compute2"),
    path('data', views.data, name="data"),
    path('save_data', views.save_data, name="save_data"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)