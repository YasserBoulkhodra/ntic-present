from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_teacher=models.BooleanField('is teacher',default=False)
    is_student=models.BooleanField('is student',default=False)
    is_headdep=models.BooleanField('is head of departement',default=False)
    phone = models.CharField(max_length=11)
    birthday = models.DateField(null=True)
    grade = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name='user_grades')
    level = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True, related_name='user_levels')

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(choices=(('L1','L1'),('L2','L2'),('L3','L3'),('M1','M1'),('M2','M2')), max_length=50, default='L1')
    phone = models.CharField(max_length=11)
    birthday = models.DateField(null=True)
    
    def __str__(self):
        return self.first_name , self.last_name , self.level , self.phone , self.birthday
    
    
    
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    birthday = models.DateField(null=True)
    grade = models.CharField(choices=(('Professor','Professor'),('doctor','doctor'),('MBA','MBA'),('MBB','MBB')), max_length=50,default='MBA')
    
    def __str__(self):
        return self.first_name , self.last_name , self.phone , self.birthday , self.grade
    

