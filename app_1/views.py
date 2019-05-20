from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q, OuterRef, Subquery
import json

from app_1.models import Art, Bigtext, Server, OS
import base64


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
    title = request.POST.get("title")
    editor1 = request.POST.get("editor1")
    obj = Bigtext()
    obj.title = title
    obj.data = editor1
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
    if request.POST.get("os_name"):
        name = request.POST.get("os_name")
        version = request.POST.get("os_version")
        os = OS()
        os.os_name = name
        os.os_version = version
        os.save()
        return HttpResponse("Saved your info.")
    items = OS.objects.all()
    arts = Art.objects.all()
    comments = Bigtext.objects.all()
    return render(request, 'app_1/server.html', {
        "items": items,
        "arts": arts,
        "comments": comments,
    })


def compute_server(request):
    name = request.POST.get("name")
    os = request.POST.get("os")
    art = request.POST.get("art")
    comment = request.POST.get("comment")
    obj = Server()
    obj.name = name
    os_obj = OS.objects.get(id=int(os))
    obj.os = os_obj
    art_obj = Art.objects.get(id=int(art))
    obj.art = art_obj
    bigtext_obj = Bigtext.objects.get(id=int(comment))
    obj.comment = bigtext_obj
    obj.save()
    return render(request, 'app_1/index.html', {})


def datepicker(request):
    return render(request, 'app_1/datepicker.html', {})


def queryset(request):
    # Sample
    # MyModel.object.filter(pk=1).delete()
    # MyModel.object.all().delete()
    #
    # qs = Server.objects.filter(name__startswith="SRV")
    qs = Server.objects.all()
    # qs = Server.objects.filter(name__contains="MM")
    # OR
    # qs = Server.objects.filter(name__contains="MM") | Server.objects.filter(name__contains="S")
    # qs = Server.objects.filter(Q(name__contains="MM") | Q(name__contains="S"))
    # AND
    # qs = Server.objects.filter(name__startswith="M") & Server.objects.filter(name__endswith="r")
    # qs = Server.objects.filter(name__startswith="M", name__endswith="r")
    #
    # qs = Server.objects.filter(name__iexact="srV_sMm")  # no sensitive (insensitive)
    # qs = Server.objects.filter(~Q(os_id__gt=4))  # NOT
    # union
    # qs_1 = Server.objects.filter(os_id__gt=4)
    # qs_2 = Server.objects.filter(os_id__lte=4)
    # qs = qs_1.union(qs_2)
    #
    # qs = Server.objects.filter(os_id__gt=4).values("name", "art_id")
    #
    # qs = Server.objects.filter(comment_id__in=[10]).values("name", "os_id")
    #
    # Subquery
    # qs1 = OS.objects.all()
    # qs = Server.objects.filter(os_id__in=Subquery(qs1.values('id')))
    # OS[all_field]+Server[name_field]
    # queryset = Server.objects.filter(os_id=OuterRef("pk")).order_by("-art_id")
    # qsqs = OS.objects.all().annotate(most_os_server=Subquery(queryset.values('name')[:1]))

    contents = {
        "queryset_count": qs.count(),
        "queryset_all": qs,
    }
    return render(request, 'app_1/queryset.html', contents)


def flex(request):
    text = "data to be encoded"
    encoded = base64.b64encode(b'data to be encoded')
    enc = request.POST.get("data")

    decode_data = ""
    if enc != None:
        decode_data = base64.b64decode(enc)

    return render(request, "app_1/flex.html", {
        "text": text,
        "encoded": encoded,
        "server_received": decode_data,
    })




