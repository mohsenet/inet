from django.urls import path

from app_1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index_2', views.index_2, name="index_3"),
    path('compute', views.compute, name="compute"),
    path('simple_upload', views.simple_upload, name="simple_upload"),
    path('table_show', views.table_show, name="table_show"),
    path('ajax1', views.ajax1, name="ajax1"),
    path('ajax2', views.ajax2, name="ajax2"),
    path('ajax2_json_response', views.ajax2_json_response, name="ajax2_json_response"),
    path('ajax2_text_response', views.ajax2_text_response, name="ajax2_text_response"),
    path('compute2', views.compute2, name="compute2"),
    path('data', views.data, name="data"),
    path('save_data', views.save_data, name="save_data"),
    path('test', views.test, name="test"),
    path('Desktop_slider', views.Desktop_slider, name="Desktop_slider"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)