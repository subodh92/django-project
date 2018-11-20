from django.shortcuts import render
import datetime
# Create your views here.
def template_wish_view(request):
    dt=datetime.datetime.now()
    t=int(dt.strftime('%H'))
    msg="hello guest !!! very  good"
    if t<12:
        msg=msg+"morning"
    elif t<16:
        msg=msg+"afternoon"
    elif t<21:
        msg=msg+"evening"
    else:
        msg=msg+"night"
    return render(request,'results.html',{'msg':msg,'date':dt})
