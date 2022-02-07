from django.shortcuts import render
from .forms import PersonForm2
from .models import Person2


def display_form2(request):
    form = PersonForm2()
    if request.method == 'POST':
        form = PersonForm2(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            comment = form.cleaned_data['comment']
            person = Person2()
            person.full_name=full_name
            person.email_address = email_address
            person.comment = comment
            person.save()
            return render(request, 'app9_2/display_person2.html', {'person':person})
    return render(request, 'app9_2/person_form2.html', {'form':form})