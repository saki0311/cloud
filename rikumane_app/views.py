from django.shortcuts import render
from rikumane_app import calendar
from .data import company_data

def index(request):
    elem = company_data[0]
    d = {
        "Company":elem['Company'],
        "URL":elem['URL'],
        "id":elem['id'],
        "Events":elem['Events'][0]['イベント名']
    }
    return render(request,'index.html',d)

#########元のmasterの書き方
#from rikumane_app import data
# Create your views here.
#def index(request):
#    return render(request,'rikumane_app/index.html',{'data.company_data':data.company_data})
#########################