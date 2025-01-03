from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
# Create your views here.

def Home(request):
    return HttpResponse("This is my first project file")


def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()
        return render(request, 'form.html', {'form': form})
    else:
        form = StudentForm() 
    return render(request, 'form.html', {'form': form})