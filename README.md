# Learning Django REST Framework (DRF) - Step-by-Step

Welcome! If you are learning how to build REST APIs in Python using **Django** and **Django REST Framework (DRF)**, this project is designed specifically for you. 

Instead of showing just one way to build APIs, this project is organized like a learning curriculum. It takes you from the most explicit, basic way (Function-Based Views) to the most advanced, automated way (Generic Views).

---

## How to Use This Project to Learn DRF

The code is divided into four main applications, ordered from **easiest/most basic** to **most advanced**. We recommend exploring them in this order:

### Step 1: Students App (`students`) — Function-Based Views (FBV)
* **What to look at**: `django_rest_main/api/views.py` (look for `studentsView` and `studentDetailView`).
* **Why it's great for beginners**: It uses standard Python functions decorated with `@api_view`. You manually write the `if request.method == 'GET':` logic. This is the best way to understand exactly how HTTP requests and responses work behind the scenes.

### Step 2: Employees App (`employees`) — Class-Based Views (CBV)
* **What to look at**: `django_rest_main/api/views.py` (look for `class Employee` and `class EmployeeDetails`).
* **Why it's great for beginners**: Instead of writing `if` statements for HTTP methods, you organize your logic into a Python class using DRF's `APIView`. The class has dedicated methods like `def get(self, request):` and `def post(self, request):`.

### Step 3: Products App (`learn_mixins`) — Mixins
* **What to look at**: `django_rest_main/api/views.py` (look for `class ProductList` and `class ProductDetails`).
* **Why it's great for beginners**: Writing CRUD (Create, Read, Update, Delete) code gets repetitive. Mixins are pre-written blocks of code provided by DRF that handle listing, creating, retrieving, updating, and deleting automatically. You just hook them together!

### Step 4: Book App (`Book`) — Generic Views (The Modern Way)
* **What to look at**: `django_rest_main/api/views.py` (look for `BookListCreateView` and `BookDetailsView`).
* **Why it's great for beginners**: This is the ultimate "Django magic" way. By subclassing views like `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView`, you only need to write **3 lines of code** to get a complete, fully-functional API! It also shows you how to connect related tables (like linking a `Book` to an `Author` using nested serializers).

---

## Core Concepts to Learn
* **Models**: Define what your database tables look like (see `Book/models.py`, `students/models.py`, etc.).
* **Serializers**: The translators of your API. They convert complex database data (Django Model instances) into standard JSON format that front-end apps (like React or mobile apps) can read, and vice-versa (see `api/serializers.py`).
* **URLs/Routing**: Mapping web addresses (like `/api/v1/books/`) to the views that handle them (see `api/urls.py`).

---

## How to Run the Project on Your Machine

### Step 1: Install Docker & Docker Compose
To run this project, we package the database (PostgreSQL) and the database viewer (pgAdmin) using Docker so you don't have to install database servers on your system.

### Step 2: Start the Project
Open your command terminal in the folder containing `docker-compose.yml` and run:
```bash
docker compose up --build
```
This will download the necessary systems and start the server!

### Step 3: Setup your Database tables (Migrations)
Open a **second** terminal window in the `django_rest_main` folder and run:
```bash
# 1. Activate your virtual environment
.\env\Scripts\Activate.ps1   # (On Windows)
source ../env/bin/activate    # (On Mac/Linux)

# 2. Run migrations to create database tables
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Populate with Dummy Data
We wrote a helpful script to fill the database with 6 ready-made dummy records for all models so you can test them immediately. Run:
```bash
python populate_db.py
```

---

## How to Test the API in Your Browser

One of DRF's best features is the **Browsable API**—an interactive webpage where you can view data and test POST/PUT/DELETE requests directly.

Open your web browser and navigate to any of these URLs:

* **Students API** (Function-Based): `http://localhost:8000/api/v1/students/`
* **Employees API** (Class-Based): `http://localhost:8000/api/v1/employees/`
* **Products API** (Mixins): `http://localhost:8000/api/v1/products/`
* **Books API** (Generic Views): `http://localhost:8000/api/v1/books/`

*(To log in as an administrator, go to `http://localhost:8000/admin/` and log in using the superuser credentials you create with `python manage.py createsuperuser`).*
