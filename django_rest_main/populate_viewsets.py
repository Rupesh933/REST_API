import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_main.settings')
django.setup()

from faker import Faker
from viewSets.models import Course, Student

fake = Faker()

def populate():
    print("Clearing existing viewSets data...")
    Student.objects.all().delete()
    Course.objects.all().delete()

    print("Generating Courses...")
    course_names = ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "History"]
    courses = []
    for name in course_names:
        course = Course.objects.create(name=name)
        courses.append(course)
    print(f"Created {len(courses)} courses.")

    print("Generating Students using Faker...")
    grades = ['A', 'B', 'C', 'D', 'F']
    students_created = 0
    for _ in range(20):
        student = Student.objects.create(
            name=fake.name(),
            age=random.randint(18, 25),
            grade=random.choice(grades),
            course=random.choice(courses)
        )
        students_created += 1

    print(f"Successfully generated {students_created} fake students!")

if __name__ == "__main__":
    populate()
