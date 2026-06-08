import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_main.settings')
django.setup()

from students.models import Students
from employees.models import Employees
from learn_mixins.models import Products
from Book.models import Author, Book

def populate():
    print("Clearing existing data...")
    Students.objects.all().delete()
    Employees.objects.all().delete()
    Products.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()

    print("Adding Students...")
    students_data = [
        {"student_id": "S001", "name": "Alice Smith", "branch": "Computer Science"},
        {"student_id": "S002", "name": "Bob Johnson", "branch": "Mechanical Eng"},
        {"student_id": "S003", "name": "Charlie Brown", "branch": "Electrical Eng"},
        {"student_id": "S004", "name": "Diana Prince", "branch": "Civil Eng"},
        {"student_id": "S005", "name": "Ethan Hunt", "branch": "IT"},
        {"student_id": "S006", "name": "Fiona Gallagher", "branch": "Chemical Eng"},
    ]
    for s in students_data:
        Students.objects.create(**s)

    print("Adding Employees...")
    employees_data = [
        {"emp_id": "E001", "emp_name": "John Doe", "designation": "Software Engineer"},
        {"emp_id": "E002", "emp_name": "Jane Smith", "designation": "Project Manager"},
        {"emp_id": "E003", "emp_name": "Mark Davis", "designation": "QA Engineer"},
        {"emp_id": "E004", "emp_name": "Sarah Connor", "designation": "System Administrator"},
        {"emp_id": "E005", "emp_name": "Bruce Wayne", "designation": "CEO"},
        {"emp_id": "E006", "emp_name": "Clark Kent", "designation": "Senior Reporter"},
    ]
    for e in employees_data:
        Employees.objects.create(**e)

    print("Adding Products...")
    products_data = [
        {"prd_id": "P001", "prd_name": "Wireless Mouse", "prd_price": 29.99, "stock": 150},
        {"prd_id": "P002", "prd_name": "Mechanical Keyboard", "prd_price": 89.99, "stock": 80},
        {"prd_id": "P003", "prd_name": "USB-C Hub", "prd_price": 19.99, "stock": 200},
        {"prd_id": "P004", "prd_name": "Gaming Headset", "prd_price": 49.99, "stock": 60},
        {"prd_id": "P005", "prd_name": "Laptop Stand", "prd_price": 34.99, "stock": 120},
        {"prd_id": "P006", "prd_name": "External SSD 1TB", "prd_price": 119.99, "stock": 45},
    ]
    for p in products_data:
        Products.objects.create(**p)

    print("Adding Authors and Books...")
    authors_data = [
        {"name": "George Orwell", "birthdate": "1903-06-25"},
        {"name": "J.K. Rowling", "birthdate": "1965-07-31"},
        {"name": "J.R.R. Tolkien", "birthdate": "1892-01-03"},
        {"name": "Agatha Christie", "birthdate": "1890-09-15"},
        {"name": "Isaac Asimov", "birthdate": "1920-01-02"},
        {"name": "Stephen King", "birthdate": "1947-09-21"},
    ]
    
    books_data = [
        {"title": "1984", "author_name": "George Orwell", "summary": "A dystopian social science fiction novel and cautionary tale.", "isbn": "9780451524935", "published": "1949-06-08", "price": 9.99},
        {"title": "Harry Potter and the Sorcerer's Stone", "author_name": "J.K. Rowling", "summary": "The first novel in the Harry Potter series.", "isbn": "9780439708180", "published": "1997-06-26", "price": 12.99},
        {"title": "The Hobbit", "author_name": "J.R.R. Tolkien", "summary": "A children's fantasy novel about the quest of home-loving hobbit Bilbo Baggins.", "isbn": "9780007440832", "published": "1937-09-21", "price": 14.99},
        {"title": "Murder on the Orient Express", "author_name": "Agatha Christie", "summary": "A detective novel featuring the Belgian detective Hercule Poirot.", "isbn": "9780062073501", "published": "1934-01-01", "price": 8.99},
        {"title": "Foundation", "author_name": "Isaac Asimov", "summary": "A science fiction novel, the first in the Foundation Trilogy.", "isbn": "9780553293357", "published": "1951-06-01", "price": 7.99},
        {"title": "The Shining", "author_name": "Stephen King", "summary": "A gothic horror novel depicting a family's stay in a haunted hotel.", "isbn": "9780307743657", "published": "1977-01-28", "price": 10.99},
    ]

    author_map = {}
    for a in authors_data:
        author_obj = Author.objects.create(**a)
        author_map[a["name"]] = author_obj

    for b in books_data:
        author_name = b.pop("author_name")
        b["author"] = author_map[author_name]
        Book.objects.create(**b)

    print("Database populated successfully with 6 dummy items for all models!")

if __name__ == "__main__":
    populate()
