from django.contrib import admin
from modelsmyapp.models import Employee,Job,Book
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','eaddr','emob','esal']

class JobAdmin(admin.ModelAdmin):
    list_display=['jpdate','jlocation','joffsal','jmob']

class CustomerAdmin(admin.ModelAdmin):
    list_display=['eno','ename','eadd','emob','esal']

class BookAdmin(admin.ModelAdmin):
    list_display=['no','title','author','publishdate']

#rmodel=[Job,Book,BookAdmin]
admin.site.register(Employee,EmployeeAdmin)
