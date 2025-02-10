from django.db import models


# Create your models here.

class Student(models.Model):
    
    S_name=models.CharField(max_length=50,null=True)
    S_dept=models.CharField(max_length=50,null=True)
    S_rollno=models.CharField(max_length=50,null=True)
    S_mobile=models.CharField(max_length=50,null=True)
    
    
    def __str__(self):
        return self.S_name +" "+ self.S_rollno