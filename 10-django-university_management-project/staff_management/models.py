from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='staff')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='staff')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
