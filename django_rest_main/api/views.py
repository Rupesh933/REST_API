from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from students.models import Students
from .serializers import StudentSerializer, EmployeeSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employees
from django.http import Http404
from learn_mixins.models import Products
from rest_framework import mixins, generics, viewsets
from Book.models import Book as BookModel, Author
from .serializers import BookSerializer, AuthorSerializer, CourseModelSerializer, StudentModelSerializer
from viewSets.models import Course, Student

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
        # print(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    

class Employee(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        seriailzer = EmployeeSerializer(data=request.data)
        if seriailzer.is_valid():
            seriailzer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(seriailzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetails(APIView):
    def get_objects(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        employee = self.get_objects(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_objects(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_objects(pk)
        employee.delete()
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    
# Mixins APIView start
class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ProductDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
# End Mixins


# Generic APIView start
# class Book(generics.ListAPIView, generics.CreateAPIView):
class BookListCreateView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

# class BookDetailsView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


# viewSets start
class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        querset = Course.objects.all()
        serializer = CourseModelSerializer(querset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CourseModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        querset = Student.objects.all()
        serializer = StudentModelSerializer(querset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        queryset = get_object_or_404(Student, pk=pk)
        serializer = StudentModelSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)