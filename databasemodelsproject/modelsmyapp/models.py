from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename=models.CharField(max_length=30)
    eaddr=models.CharField(max_length=100)
    emob=models.CharField(max_length=11)
    esal=models.FloatField()

class Job(models.Model):
    jpdate = models.DateField()
    jlocation=models.CharField(max_length=100)
    joffsal=models.FloatField()
    jmob=models.CharField(max_length=11)
    #jemail=models.EmaiField()


class Book(models.Model):
    no = models.IntegerField()
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publishdate=models.DateField()

# class customer(models.Model):
#     cname=models.CharField(max_length=30)
#     #cemail=models.EmaiField()
#     #ephon=models.PhoneField()
#     cage=models.IntegerField()
