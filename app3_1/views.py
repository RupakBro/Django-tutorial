from django.shortcuts import render


def third(request):
    return render(request, 'app3_1/Third.html')


def fourth(request):
    return render(request, 'app3_1/Fourth.html')