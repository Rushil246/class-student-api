from django.db import models

# Create your models here.

#create class models

class classes(models.Model):
    classes_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(("IT","IT",),("CE","CE"),("CSE","CSE")))
    added_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
#student
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    grade=models.CharField(max_length=50,choices=(("A","A"),("B","B"),("C","C"),("D","D")))
    classes=models.ForeignKey(to=classes,on_delete=models.CASCADE)