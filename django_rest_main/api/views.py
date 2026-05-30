from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


# def studentsView(request):
    # students = {
    #     'id':1,
    #     'name':'Rupesh Rana',
    #     'class': 'Computer Science'
    #     }
    # students = Students.objects.all()
    # print(students)
    # # return JsonResponse(students, safe=False)
    
    # # manually convert data json data into list then display in browser  not recomented this
    # students_list = list(students.values())
    # return JsonResponse(students_list, safe=False)
    
# Fuction Based View
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # get all the data from the Students table
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    
# get a single value from Student using primary key
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        students = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # if you only pass data=request.data then it create new data
        serializer = StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)