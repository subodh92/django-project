from django.shortcuts import render
import datetime
# Create your views here.
def template_view(request):
    dt=datetime.datetime.now()
    mydict={'date':dt}
    return render(request,'myapp/result.html',mydict)
