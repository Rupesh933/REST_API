from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.

def students(request):
    students = [
        {'id':1, 'name':'Rupesh Rana', 'age':23}
    ]
    return HttpResponse(students)

