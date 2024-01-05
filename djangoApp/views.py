from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("demo pagae")
def demotem(request):
    return render(request,"demo.html")