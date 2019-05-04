from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from app_1.models import Art, Bigtext


def index(request):
    return render(request, 'app_1/index_2.html')


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
    return render(request, 'app_1/ajax.html', {})


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