from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from MyApp.models import ToDoList
# Create your views here.

def get_client_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip=""
    return ip
def home(request):
    print(request.META.get('REMOTE_ADDR'))
    items = ToDoList.objects.all().order_by('-added_date')
    context = {
        'items':items,
    }
    return render(request,'home.html',context)

@csrf_exempt
def add_to_do(request):
    #content = request.POST.get('search')
    #Another method to do the same thing
    content = request.POST['search']
    ToDoList.objects.create(name=content,ip_address=get_client_ip(request))
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_to_do(request,item_id):
    ToDoList.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')
