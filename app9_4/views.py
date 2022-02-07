from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('..')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request,'app9_4/new.html',{'form':form})


def show(request):
    employees = Employee.objects.all()
    print(employees)
    return render(request,"app9_4/index.html",{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    print(employee)
    return render(request,'app9_4/edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('../show')
    return render(request, 'app9_4/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('../show')