from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

from employees.models import Employees
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
from learn_mixins.models import Products
from django.utils import timezone

class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        default=timezone.now,
        format="%d-%m-%Y %I:%M:%S %p",
        required=False
    )
    update_at = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M:%S %p"
    )
    class Meta:
        model = Products 
        fields = [
                  'id',
                  'prd_id',
                  'prd_name',
                  'stock',
                  'prd_price',
                  'update_at',
                  'created_at'
                  ]

from Book.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published', 'price', 'author']


from viewSets.models import Course, Student
class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentModelSerializer(serializers.ModelSerializer):
    course = CourseModelSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'course']