from django.db import models

# Create your models here.
class Book(models.Model):
    bName=models.CharField(max_length=100,primary_key=True)
    bAutor=models.CharField(max_length=100)
    cost=models.IntegerField()

    def __str__(self) -> str:
        return self.bName

class Subjacts(models.Model):
    bName=models.ForeignKey(Book,on_delete=models.CASCADE)
    subName=models.CharField(max_length=100)
    sMarks=models.IntegerField()
    

    def __str__(self) -> str:
        return self.subName


class Teacher(models.Model):
    subName=models.ForeignKey(Subjacts,on_delete=models.CASCADE)
    tName=models.CharField(max_length=100)
    tSub=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tName
    

class Student(models.Model):
    tName=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)
    snum=models.IntegerField()
    semail=models.EmailField()
    simg=models.ImageField()
    smarks=models.IntegerField(default=35)
    sub=models.CharField(max_length=100,default='all')

    def __str__(self) -> str:
        return self.sname
    
    
