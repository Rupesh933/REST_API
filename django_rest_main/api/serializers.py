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
class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M:%S %p"
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