from django.shortcuts import render
from django.http import HttpResponseRedirect
from testApp.models import Employee
from .forms import addform 

# Create your views here.
def home(request):
    mydata = Employee.objects.all().values()
    context = {
        'data': mydata
    }
    return render(request, 'testApp/main.html', context)

def add(request):
    if request.method=='POST':
        form  = addform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = addform()
        

    return render(request, 'testApp/add.html', {"form": form})

def update(request, id):
    mydata = Employee.objects.filter(id = id).values()
    
    context = {
        'ename' : mydata[0]['ename'],
        'edept' : mydata[0]['edept'],
        'esal'  : mydata[0]['esal']
    }

    if request.method == "POST":
        #checking does ename contains value or not
        if request.POST.get('ename',False):
            nm = request.POST.get('ename',False)
        else:
            nm = mydata[0]['ename']

        if request.POST.get('edept',False):
            dep = request.POST.get('edept',False)
        else:
            dep = mydata[0]['edept']

        if request.POST.get('esal',False):
            sal = request.POST.get('esal',False)
        else:
            sal = mydata[0]['esal']

        reg = Employee.objects.filter(id = id).update(ename = nm, edept = dep, esal = sal)
        
        return HttpResponseRedirect('/')

    return render(request, 'testapp/update.html',context)

def delete(request, id):
    deldata = Employee.objects.get(id = id)
    deldata.delete()
    return HttpResponseRedirect('/')

