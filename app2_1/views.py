from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    return render(request, 'app2_1/index.html')


def about(request):
    return render(request, 'app2_1/about.html')


def services(request):
    return render(request, 'app2_1/services.html')


def contact(request):
    return render(request, 'app2_1/contact.html')
