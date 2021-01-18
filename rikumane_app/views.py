from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime as dt
#from rikumane_app import calendar
from .data import company_data
from PIL import Image
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from rikumane_app.models import Company,ES,Event,CommonInfo,analysis_myself
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import CompanyForm
from .crud import *
from .word_cloud import *
from django.contrib.auth.models import User # Django認証用モデルのインポート
from django.contrib.auth import authenticate # 認証設定用関数のインポート
from django.contrib.auth import login as auth_login # ログイン認証用関数のインポート
from django.contrib.auth import logout # ログアウト関数のインポート
import io
import base64
<<<<<<< HEAD
import json
=======
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

>>>>>>> 6b664682d1d3296eb0152c80e8d8e76af0620d34

'''
login/logout/sineup用関数
'''
def login(request):
    # POSTパラメータの有無の確認

    if request.method=='POST':
        # ログイン用パラメータの場合
        if (request.POST.get('action') == 'login'):
            # login認証
            user = authenticate(username=request.POST['login_id'], password=request.POST['login_pass'])
            # ログイン認証に成功した場合
            if user is not None:
                if user.is_active:
                    # ログインの実行
                    auth_login(request,user)
                    # カレンダー画面へリダイレクト
                    return redirect('rikumane_app:calendar')
                # アカウントが無いユーザの場合
                else:
                    print("Your account has been disabled!")
            # IDとパスワードがない場合
            else:
                print("Your username and password were incorrect.")
        # アカウント作成パラメータの場合
        elif (request.POST.get('action') == 'create'):
            # アカウント作成
            user = User.objects.create_user(request.POST['create_name'], request.POST.get('create_id'),request.POST['create_pass'])
            CommonInfo(Account=user,MemoES='',MemoAnalysis='',Image="").save()
            # DBへ保存
            user.save()
            # カレンダー画面へリダイレクト
            return redirect('rikumane_app:calendar')
    else:
        # logoutパラメータの確認
        if (request.GET.get('logout') == 'true'):
            # Logout
            logout(request)
            # トップ（login）画面へ移動
            return redirect('rikumane_app:top')
        return render(request,'top.html')

'''
ホーム画面（カレンダー画面での操作）
'''
def calendar(request):
    if not request.user.is_authenticated:
        return redirect('rikumane_app:top')
    else:
        if request.method == 'POST':
            post_action = request.POST.get('action')
            if  post_action == "add_company":
                Company_create(request,request.user)
            elif post_action == "update_account":
                CommonInfo_update(request,request.user)
            elif post_action == "prof_edit":
                Account_update(request)
        Company_list = Company.objects.all().filter(Account_id=request.user.id)
        Events_list = []
        for one in Company_list:
            event_list = Event.objects.all().filter(Company=one)
            if event_list != []:
                for event in event_list: 
                    Events_list.append(event)
        d = {
            'data':Company_list,
            'user':request.user,
            'common':CommonInfo.objects.get(id=request.user.id),
            'events':Events_list
            }
        return render(request,'calendar.html',d)
'''
index用関数　企業データを全てindexに返す
'''
def index(request):
    if not request.user.is_authenticated:
        return redirect('rikumane_app:top')
    else:
        if request.method == 'POST':
            post_action = request.POST.get('action')
            if  post_action == "add_company": # 企業登録のイベント
                Company_create(request,request.user)
            elif post_action == "update_account": # アカウント情報更新イベント
                CommonInfo_update(request,request.user)
            elif post_action == "edit-company": # 企業情報編集イベント
                Company_update(request,request.user)
            elif post_action == "delete-company": # 企業情報削除イベント
                Company_delete(request,request.user)
            elif post_action == "update-company-data": # 企業詳細情報更新イベント
                Company_data_update(request)
            elif post_action == "add_event": # イベント追加
                Event_create(request)
            elif post_action == "event_delete": # イベント削除
                Event_delete(Event.objects.get(id=request.POST.get('event_id')))
        company = Company.objects.get(Account_id=request.user.id,id=request.GET.get('id'))
        Events = Event.objects.all().filter(Company=company).order_by('EventEnd')
        if len(Events) > 0:
            for event in Events:
                event.time = event.EventEnd
                event.EventEnd = event.EventEnd.strftime('%Y/%m/%d')
        
        Flows = Event.objects.all().filter(Company=company,Flow=True).order_by('EventEnd')
        if len(Flows) > 0:
            for flow in Flows:
                flow.EventEnd = flow.EventEnd.strftime('%Y/%m/%d')

        d = {
            'data':Company.objects.all().filter(Account_id=request.user.id),
            'user':request.user,
            'common':CommonInfo.objects.get(id=request.user.id),
            'company':company,
            'events':Events,
            'flows':Flows,
            }
        return render(request,'index.html',d)

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

    return render(request,'detail.html',d)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('rikumane_app:top')
    if request.method == 'POST':
        data = CommonInfo.objects.get(Account_id=request.user.id)
        data.MemoAnalysis = request.POST.get('self_analysis')
        data.MemoES = request.POST.get('entrysheet')
        data.Memo = request.POST.get('memo')
        data.save()
    else:
        data = CommonInfo.objects.get(Account_id=request.user.id)
    d = {
        'common':data,
        'data':Company.objects.all().filter(Account_id=request.user.id),
        # 'common.MemoAnalysis':data.MemoAnalysis,
        # 'common.MemoES':data.MemoES,
        # 'common.Memo':data.Memo,
    }
    # print(d['common'].Memo)
    return render(request,'profile.html',d)

def get_svg():
    generate_wc("こんにちは")
    # 以下ますい追記部分
    buffer = io.BytesIO() # メモリ上への仮保管先を生成
    plt.savefig(buffer, format="PNG")
    base64Img = base64.b64encode(buffer.getvalue()).decode().replace("'", "")

    return base64Img



def analysis_self(request):
    if not request.user.is_authenticated:
        return redirect('rikumane_app:top')
    else:
        if request.method == 'POST':
            d = analysis_myself(
                Account=request.user,
                Title=request.POST.get('title'),
                Content=request.POST.get('content'),
                Motivation=request.POST.get('motivation'),
                Start_time=request.POST.get('start_time'),
                End_time=request.POST.get('end_time')
            )
            d.save()
            return redirect('rikumane_app:analysis_self')
        motiGraphBase64 = get_svg() # base64エンコードされた文字列を受け取り
        json_data = json.dumps(list(data.values()))
        d = {
            'data':analysis_myself.objects.filter(Account_id=request.user.id),
            'now':timezone.now,
            'data_json':json_data,
            "motiGraphBase64": motiGraphBase64
        }
        return render(request, 'analysis_self.html',d)

def matching_output(request):
    if not request.user.is_authenticated:
        return redirect('rikumane_app:top')
    else:
        return render(request, 'matching_output.html')
