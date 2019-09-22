from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from MyApp.models import ToDoList
# Create your views here.
def home(request):
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
    ToDoList.objects.create(name=content)
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_to_do(request,item_id):
    ToDoList.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')
