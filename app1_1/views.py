from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    str1 = "<h1>Welcome to sample site!</h1>"
    str1 += "<h3><a href='about'>About Us</a></h3>"
    str1 += "<h3><a href='serivces'>Services</a></h3>"
    return HttpResponse(str1)

def about(request):
    str1 = "<h2>About Us</h2>"
    str1+="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    str1 +='<p><a href="../app1_1">Index</a></p>'
    str1 +='<p><a href="serivces">Services</a></p>'
    return HttpResponse(str1)

def services(request):
    str1 = "<h2>Our Services</h2>"
    str1+="""Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32."""
    str1 += '<p><a href="../app1_1">Index</a></p>'
    str1 += '<p><a href="about">About Us</a></p>'
    return HttpResponse(str1)
