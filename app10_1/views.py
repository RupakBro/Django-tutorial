from django.views.generic import CreateView # Insert New
from django.views.generic import ListView # Get All Persons
from django.views.generic import DetailView # Details of Individual
from django.views.generic import UpdateView # Update/Edit Person
from django.views.generic import DeleteView # Delete Person
from django.urls import reverse_lazy # Helper of DeleteView

from .models import Person


class PersonCreate(CreateView):
    model = Person
    fields = ['full_name', 'contact_address', 'email', 'mobile']
    template_name = 'app10_1/person_form.html'
    success_url = '..'


class ListPersons(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

class PersonUpdate(UpdateView):
    model = Person
    fields = ['full_name', 'contact_address', 'email', 'mobile']
    template_name = 'app10_1/person_form.html'
    success_url = '../../'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')