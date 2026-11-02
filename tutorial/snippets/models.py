from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.roll}"

    class Meta:
        ordering = ['roll']