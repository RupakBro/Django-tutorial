from django.shortcuts import render
from django.http import HttpResponse

def bootstrap1(request):
    return render(request, 'app4_2/document1.html')


def bootstrap2(request):
    return render(request, 'app4_2/document2.html')