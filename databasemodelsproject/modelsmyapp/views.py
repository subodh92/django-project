from django.shortcuts import render
from modelsmyapp.models import Employee
# Create your views here.
def employee_details_view(request):
    empdetails=Employee.objects.all()
    return render(request,'index.html',{'employeedetails':empdetails})
