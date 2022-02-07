from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .models import Student
from .models import Client


# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request, 'app8_1/index.html', {'persons': persons})


def display_new(request):
    return render(request, 'app8_1/add_new.html')


def insert(request):
    if request.method == 'GET':
        person = Person()
        person.pid = request.GET.get('txt_id')
        person.full_name = request.GET.get('txt_name')
        person.contact_address = request.GET.get('txt_address')
        person.save()
    else:
        person = Person()
        person.pid = request.POST.get('txt_id')
        person.full_name = request.POST.get('txt_name')
        person.contact_address = request.POST.get('txt_address')
        person.save()
    return HttpResponseRedirect("..")


def display_edit(request):
    pid = request.GET.get('pid')
    person = Person.objects.get(pid=pid)
    print("For Edit ", person)
    return render(request, 'app8_1/edit.html', {'person': person})


def update(request):
    pid = request.POST.get('txt_id')
    person = Person.objects.get(pid=pid)
    person.full_name = request.POST.get('txt_name')
    person.contact_address = request.POST.get('txt_address')
    person.save()
    return HttpResponseRedirect("..")

def display_delete(request):
    pid = request.GET.get('pid')
    person = Person.objects.get(pid=pid)
    return render(request, 'app8_1/delete.html', {'person': person})


def display_delete_confirm(request):
    pid = request.POST.get('txt_id')
    print("pid -> ", pid)
    return render(request, 'app8_1/display_confirmation.html', {'pid': pid})


def delete(request):
    pid = request.POST.get('txt_id')
    person = Person.objects.get(pid=pid)
    person.delete()
    return HttpResponseRedirect("..")


def crud(request):
# Save Record
    person1 = Person(pid=1, full_name="Raj Rai", contact_address="Kthmandu Nepal")
    #person1.save()

    person2 = Person()
    person2.pid=2
    person2.full_name="Kiran Rai"
    person2.contact_address="Lalitpur, Nepal"
    #person2.save()

    clien1 = Client(full_name='Rhydam', contact_address='Kathmandu')
    #clien1.save()

    clien2 = Client()
    clien2.full_name="Rima"
    clien2.contact_address = "Lalitpur"
    clien2.save()
    print(clien2.id)# Return the id which lastely entered on table

    person1 = Person(pid=1, full_name="Raj Rai", contact_address="Kthmandu")
    person1.save()

    person2 = Person()
    person2.pid=2
    person2.full_name="Kiran Rai"
    person2.contact_address="Lalitpur"
    person2.save()

    person3 = Person.objects.create(pid=3, full_name='Reema Thapa',contact_address='Bhaktapur')

# Select or Filter Records
    # indexing
    # Select All
    all_clients = Client.objects.all()
    for client in all_clients:
        print(client)

    # Get Value
    client = Client.objects.get(pk=1)
    print(client)

    # Filter # Slicing
    result = Client.objects.filter(id=1)
    result = Client.objects.filter(id=175)
    result = Client.objects.filter(full_name='UTSAV')
    result = Client.objects.filter(full_name__exact='UTSAV')
    result = Client.objects.filter(full_name__contains='UTSAV')
    result = Client.objects.filter(id=231, full_name__contains='UTSAV')
    result = Client.objects.filter(contact_address__contains='DOL').filter(full_name__contains='UT')
    result = Client.objects.all().exclude(id = 20)

    result = Client.objects.exclude(contact_address='GORKHS')
    result = Client.objects.exclude(id__gt=50)
    result = Client.objects.filter(id__gt=50)
    result = Client.objects.filter(contact_address='GORKHA')
    result = Client.objects.filter(id__in=[2, 3])
    result = Client.objects.filter(full_name__endswith='A')
    result = Client.objects.filter(full_name__startswith='A')

    for item in result:
        print(item)

    # Order By
    result = Client.objects.all().order_by('id')
    result = Client.objects.all().order_by('-id')
    result = Client.objects.order_by('-id').order_by('full_name').order_by('contact_address')

    # Result to Dict
    results = Client.objects.values()
    print(type(results))
    print(type(results[0]))
    #return render(request, "app8_1/index.html", {'results':results})

    # Result to List
    results = Client.objects.all()
    print(type(results))
    print(type(results[0]))
    client = results[0]
    print(type(client))
    print(client.id, client.full_name, client.contact_address)
    #return render(request, "app8_1/index.html", {'results':results})

# Update
    # Individual Object Update
    client = Client.objects.get(id=1)
    client.full_name="RAJ THAPA"
    client.contact_address="POKHARA, KASKI, NEPAL"
    client.save()

    # client = Client.objects.get(id=1)
    # client.full_name = "RAJ"
    # client.save()

    # client = Client.objects.get(id=1)
    # client.contact_address = "POKHARA"
    # client.save()

    #Bulk Update
    #Client.objects.select_for_update().filter(contact_address__contains='GOR').update(contact_address='PATAN')

# Delete
    # Individual Delete
    # client = Client.objects.get(id = 1)
    # client.delete()

    # Bulk Delete
    # Client.objects.select_for_update().filter(contact_address__contains='GOR').delete()
    return HttpResponse("Hello from Model CRUD")