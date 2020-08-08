from django.shortcuts import render
from rikumane_app import data


# Create your views here.
def index(request):
    return render(request,'rikumane_app/index.html',{'data.company_data[0]':data.company_data})