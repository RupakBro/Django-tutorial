from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world of Django 3.1")