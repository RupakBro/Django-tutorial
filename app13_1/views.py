from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.staticfiles.storage import staticfiles_storage
import csv
from reportlab.pdfgen import canvas # pip install reportlab


def index(request):
    return render(request, 'app13_1/index.html')


def create_image(request):
    file_path = staticfiles_storage.path('app13_1/images/image_1.png')
    image_data = open(file_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data1.csv"'
    writer = csv.writer(response)
    writer.writerow(['Row1', 'Raj', 'Thapa', '9851145433'])
    writer.writerow(['Row2', 'Rajan', 'Rai', '9843232321', 'rajan@gmail.com'])
    return response


def create_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document1.pdf"'
    p = canvas.Canvas(response)
    p.drawString(50, 800, "Hello world of python!")
    p.showPage()
    p.save()
    return response