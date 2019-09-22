from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,'home.html')

@csrf_exempt
def add_to_do(request):
    print("todo")
    return HttpResponseRedirect('/')
