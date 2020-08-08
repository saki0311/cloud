from django.shortcuts import render
from rikumane_app import data


# Create your views here.
def index(request):
    params = {
        'Company0': data.company_data[0]['Company'],
        'URL0': data.company_data[0]['URL'],
        'ID0': data.company_data[0]['id'],
    }
    return render(request,'rikumane_app/index.html', params)

def ivents(request):
    return render(request,'rikumane_app/ivents.html')