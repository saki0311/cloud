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
    params = {
        'data':company_data
    }
    return render(request,'ivents.html',params)

def add_event(request):
    d={
        'title':request.GET.get('name'),
        'start_time':request.GET.get('start_time'),
        'end_time':request.GET.get('end_time'),
    }
    
    
    if request.GET.get('name') and request.GET.get('start_time') and request.GET.get('end_time'):
        d['start_time'] += ":00"
        d['end_time'] += ":00"
        event = calendar.credentials_account()
        calendar.add_calendar(event,d)
    return render(request,'add_event.html',d)