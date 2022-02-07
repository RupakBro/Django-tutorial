from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person


def index(request):
    return HttpResponse("Hello from App9_1")


def display_form1(request):
    form1 = PersonForm()
    return render(request, 'app9_1/person_form1.html', {'form':form1})


def get_form1(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        contact_address = request.POST.get('contact_address')
    else:
        full_name = request.GET.get('full_name')
        contact_address = request.GET.get('contact_address')

    person = Person()
    person.full_name=full_name
    person.contact_address = contact_address
    person.save()# Save record on database
    context = {
        'id': person.id,
        'full_name': full_name,
        'contact_address': contact_address,
    }
    return render(request, 'app9_1/display_person1.html', context)