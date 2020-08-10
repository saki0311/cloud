from django.shortcuts import render
from rikumane_app import calendar
from .data import company_data
from . import models

'''
index用関数　企業データを全てindexに返す
'''
def index(request):
    params = {
        'data':company_data,
    }
    return render(request,'index.html', params)

'''
・ivents用関数　
- 選択したクエリパラメータと同じidをもつ企業だけを抽出して
  detail.htmlへ返す
- 入力したカレンダーの予定をGoogleAPIと連携して自分のカレンダーへ登録

・変数名　
comapny -> 選択中の企業の辞書
data -> 全ての企業データ
title -> 予定名
start_time -> 予定開始時刻
end_time -> 予定終了時刻
'''

def detail(request):
    con = int(request.GET.get('id'))
    for one in company_data:
        if one['unique_id'] == con:
            res = one
            break
    d={
    'data':company_data,
    'title':request.GET.get('name'),
    'start_time':request.GET.get('start_time'),
    'end_time':request.GET.get('end_time'),
    'company':res,
    }
    if request.GET.get('name') and request.GET.get('start_time') and request.GET.get('end_time'):
        d['start_time'] += ":00"
        d['end_time'] += ":00"
        event = calendar.credentials_account()
        calendar.add_calendar(event,d)

    return render(request,'detail.html',d)