from django.shortcuts import render
from rikumane_app import calendar
from .data import company_data

def index(request):
    params = {
        'Company0': company_data[0]['Company'],
        'URL0': company_data[0]['URL'],
        'ID0': company_data[0]['id'],
    }
    return render(request,'index.html', params)

def ivents(request):
    return render(request,'ivents.html')

