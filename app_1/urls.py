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
    path('mandaliof', views.mandaliof, name="mandaliof"),
    path('ckeditor', views.ckeditor, name="ckeditor"),
    path('compute_ckeditor', views.compute_ckeditor, name="compute_ckeditor"),
    path('get_ckeditor', views.get_ckeditor, name="get_ckeditor"),
    path('menufullscreen', views.menufullscreen, name="menufullscreen"),
    path('cart_1', views.cart_1, name="cart_1"),
    path('list', views.list, name="list"),
    path('server', views.server, name="server"),
    path('compute_server', views.compute_server, name="compute_server"),
    path('datepicker', views.datepicker, name="datepicker"),
    path('queryset', views.queryset, name="queryset"),
    path('flex', views.flex, name="flex"),
    path('class_concept', views.class_concept, name="class_concept"),
    path('audio', views.audio, name="audio"),
    path('Normal_Distribution_Table', views.Normal_Distribution_Table, name="Normal_Distribution_Table"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)