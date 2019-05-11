from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from app_1.models import Art, Bigtext, Server


def index(request):
    return render(request, 'app_1/index.html')


def index_2(request):
    return render(request, 'app_1/index_2.html')


def test(request):
    return render(request, 'app_1/test.html', {})

def Desktop_slider(request):
    return render(request, 'app_1/Desktop_slider.html', {})


def data(request):
    return render(request, 'app_1/data.html', {})


def save_data(request):
    title = request.POST.get("title")
    data = request.POST.get("data")
    obj = Bigtext(title=title, data=data)
    obj.save()
    return HttpResponse(data)


def compute2(request):
    ip = request.POST.get("ip")
    return HttpResponse("Your ip is:" + str(ip))


def ajax1(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        return HttpResponse(title)
    return render(request, 'app_1/ajax1.html', {})


def ajax2(request):
    return render(request, 'app_1/ajax2.html', {})


def ajax2_json_response(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        return JsonResponse({"title": title})
    return render(request, 'app_1/ajax2.html', {})


def ajax2_text_response(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        return HttpResponse(title)
    return render(request, 'app_1/ajax2.html', {})


def table_show(request):
    # contact_list = Art.objects.all()
    contact_list = Art.objects.get_queryset().order_by('id')
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'app_1/table.html', {'contacts': contacts})


def table_show_(request):
    return render(request, 'app_1/table.html', {})


def compute(request):
    ip = request.POST.get("ip")
    port = request.POST.get("port")
    obj = Art(ip=ip, port=port)
    obj.save()
    return render(request, 'app_1/info.html', {})


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'app_1/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'app_1/simple_upload.html')
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return render(request, 'app_1/simple_upload.html', {
            "uploaded_file_url": uploaded_file_url
        })
    return render(request, 'app_1/simple_upload.html')


def mandaliof(request):
    return render(request, 'app_1/mandaliof.html', {})


def ckeditor(request):
    contacts = Bigtext.objects.all()
    return render(request, 'app_1/ckeditor.html', {"contacts": contacts})


def compute_ckeditor(request):
    obj = Bigtext(title="0", data=request.POST.get("editor1"))
    obj.save()
    return render(request, 'app_1/index.html', {})

# todo: Bigtext.objects.get(request.pk)
def get_ckeditor(request):
    val = request.POST.get("selected_item")
    app_20 = Bigtext.objects.get(pk=int(val))
    data3 = app_20.data
    return HttpResponse(data3)


def menufullscreen(request):
    return render(request, 'app_1/menufullscreen.html', {})


def cart_1(request):
    return render(request, 'app_1/cart_1.html', {})


def list(request):
    return render(request, 'app_1/list.html', {})


def server(request):
    return render(request, 'app_1/server.html', {})


def compute_server(request):
    name = request.POST.get("name")
    os =request.POST.get("os")
    obj = Server(name=name, os=os)
    obj.save()

    return render(request, 'app_1/index.html', {})




