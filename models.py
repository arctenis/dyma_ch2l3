from django.db import models


class Group(models.Model):
    GRADES = (
        ("2", "Seconde"),
        ("1", "Première"),
        ("T", "Terminale"),
    )
    number = models.PositiveIntegerField()
    grade = models.CharField(max_length=1, choices=GRADES)
    main_teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.grade}e{self.number}"


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    discipline = models.CharField(max_length=64)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return f"Pr. {self.first_name} {self.last_name}"
