from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def home_page_view(request):
    return render(request,'home.html')
def sports_view(request):
    news1="Viart Kohal become scond batsman who made 36+ hundred in oneday cricket match"
    news2="MS Dhoni is droped for austrailia tour"
    news3="Risabh Pant make his first fifty in international t-20 game "
    news4="Dinesh Kartik is selected to play for austarilia tour "
    mydict={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'sports.html',mydict)

def politics_view(request):
    #mydict={'hell':'subodh'}
    return render(request,'politics.html')


def technichal_view(request):
    #mydict={'hell':'subodh'}
    return render(request,'technichal.html')
