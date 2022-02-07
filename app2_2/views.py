from django.shortcuts import render

def index(request):
    return render(request, 'app2_2/index.html')

def generic(request):
    return render(request, 'app2_2/generic.html')

def elements(request):
    return render(request, 'app2_2/elements.html')