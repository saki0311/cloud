from django.shortcuts import render
from rikumane_app import calendar
from .data import company_data

def index(request):
    params = {
        'data':company_data,
    }
    return render(request,'index.html', params)

def detail(request):
    con = int(request.GET.get('id'))
    for one in company_data:
        if one['unique_id'] == con:
            res = one['info']
            break
    params = {
        'company':res,
        'data':company_data,
    }
    return render(request,'detail.html', params)


def ivents(request):
    d={
    'data':company_data,
    'title':request.GET.get('name'),
    'start_time':request.GET.get('start_time'),
    'end_time':request.GET.get('end_time'),
    }
    if request.GET.get('name') and request.GET.get('start_time') and request.GET.get('end_time'):
        d['start_time'] += ":00"
        d['end_time'] += ":00"
        event = calendar.credentials_account()
        calendar.add_calendar(event,d)

    return render(request,'ivents.html',d)