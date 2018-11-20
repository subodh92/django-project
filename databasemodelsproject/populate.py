import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','databasemodelsproject.settings')
django.setup()
from faker import Faker
from random import *
from modelsmyapp.models import *
fake=Faker()
def mobilenumber():
    m=randint(6,9)
    mob=str(m)
    for i in range(9):
        mob+=str(i)
    return mob

def populate(n):
    for i in range(n):
        feno=randint(1001,99999)
        fename=fake.name()
        fesal=randint(10000,999999)
        feaddr=fake.city()
        fmob=mobilenumber()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr,emob=fmob)
populate(30)
