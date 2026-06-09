from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course', views.CourseViewSet, basename='course')
router.register('student', views.StudentViewSet, basename='student')

urlpatterns=[
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    
    # employee path  and this is a CBVs and treat as a CBVs
    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),

    # Product path, here we used Mixins topics
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetails.as_view()),

    # Book path, here we used Generic APIView
    path('books/', views.BookListCreateView.as_view()),
    path('books/<int:pk>/', views.BookDetailsView.as_view()),

    # ViewSets path
    path('', include(router.urls)),
    path('v1/', include(router.urls))

]