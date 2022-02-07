from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import requests


api_url = 'http://localhost:8000/app16_1/customers/'


def index(request):
    response = requests.get(api_url)
    records = response.text
    records = json.loads(records) #Text to Dictionary
    return render(request, 'app16_2/index.html', {'persons': records})


def display_new_form(request):
    if request.method =='POST':
        fullname = request.POST.get('txt_name')
        address = request.POST.get('txt_address')
        record = {'fullname': fullname, 'address': address}
        print(record)
        response = requests.post(api_url, json=record)
        print(response)
        if response.status_code == 201:
            result = True
        else:
            result = False
        return render(request, 'app16_2/result.html', {'title': 'Record insert!', 'status': result})
    return render(request, 'app16_2/new.html')


def update(request):
    if request.method == 'POST':
        id = request.POST.get('txt_id')
        fullname = request.POST.get('txt_name')
        address = request.POST.get('txt_address')
        record = {'id':id, 'fullname': fullname, 'address':address}
        tmp_api_url = api_url + str(id) + '/'
        response = requests.put(tmp_api_url, json=record)
        if response.status_code == 200:
            result = True
        else:
            result = False
        return render(request, 'app16_2/result.html', {'title': 'Record update!', 'status': result})
    # Search Record and Display for Edit
    id = request.GET.get('id')
    response = requests.get(api_url + str(id))
    record = json.loads(response.content)
    print(type(record))
    print(record)
    return render(request, 'app16_2/edit.html', {'contact': record})


def delete(request):
    # Search Record and Display for Edit
    id = request.GET.get('id')
    tmp_api_url = api_url + str(id) + '/'
    response = requests.delete(tmp_api_url)
    if response.status_code == 200:
        result = True
    else:
        result = False
    return render(request, 'app16_2/result.html', {'title': 'Record delete!', 'status': result})