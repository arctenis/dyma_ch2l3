import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()

from faker import Faker
from students.models import Student, Group, Teacher
from datetime import datetime

fake = Faker()

disciplines = ["Maths", "Histoire", "Espagnol", "Physique", "Français"]

# Créer 10 profs
teachers = [
    Teacher(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date_of_birth(tzinfo=None, minimum_age=30, maximum_age=60),
        discipline=fake.random_element(elements=disciplines),
    )
    for _ in range(10)
]
Teacher.objects.bulk_create(teachers)

# Créer 5 groupes numérotés de 1 à 5 pour chaque niveau
groups = [
        Group(number=number,
              grade=grade,
              main_teacher=fake.random_element(teachers))
        for number in range(1, 6) for grade in ("2", "1", "T")
        ]

Group.objects.bulk_create(groups)

# Affecter des groupes à chaque prof
for teacher in teachers:
    teacher.groups.add(
        *fake.random_elements(
            elements=groups, length=fake.random_int(min=3, max=7), unique=True
        )
    )

# Créer 100 étudiants
students = [
    Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=18),
        group=fake.random_element(groups),
    )
    for _ in range(100)
]

Student.objects.bulk_create(students)
