from django.urls import path
from . import views

urlpatterns=[
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    
    # employee path  and this is a CBVs and treat as a CBVs
    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
]