from django.db import models


class Student(models.Model):
    student_first_name = models.CharField(max_length=200)
    student_last_name = models.CharField(max_length=200)
    student_email = models.EmailField()

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name

class Program_Of_Study(models.Model):
    student = models.ForeignKey(Student)
    advisor = models.CharField(max_length=200)
