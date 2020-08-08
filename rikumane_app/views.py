from django.shortcuts import render
from rikumane_app import calendar
from .data import company_data

def index(request):
    params = {
        'Company0': data.company_data[0]['Company'],
        'URL0': data.company_data[0]['URL'],
        'ID0': data.company_data[0]['id'],
    }
    return render(request,'rikumane_app/index.html', params)

def ivents(request):
    return render(request,'rikumane_app/ivents.html')

