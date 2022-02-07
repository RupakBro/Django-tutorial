from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    id = request.GET.get("id") # Get value from url
    name = request.GET.get("name")  # Get value from url
    #print(id, name)
    return HttpResponse(id+", "+name)


def display_form1(request):
    return  render(request, 'app4_1/form1.html')


def get_values1(request):
    # getting values from html form
    id = request.GET.get("id")
    name = request.GET.get("name")
    # display values
    return HttpResponse(id+", "+name)

def get_values2(request):
    # getting values from html form
    id = request.POST.get("id")
    name = request.POST.get("name")
    # display values
    return HttpResponse(id+", "+name)