from django.shortcuts import redirect, render
#from rikumane_app import calendar
from .data import company_data
from rikumane_app.models import Company,Account,ES,Event
# from .forms import CompanyForm
from .crud import *
from django.contrib.auth.models import User # Django認証用モデルのインポート
from django.contrib.auth import authenticate # 認証設定用関数のインポート
from django.contrib.auth import login as auth_login # ログイン認証用関数のインポート
from django.contrib.auth import logout # ログアウト関数のインポート

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
            user = Account.objects.get(id=0)
            print(user)
            print(request.user.id)
            Company_create(request,request.user)
        return render(request,'calendar.html')

'''
プロフィール画面
'''
def profile(request):
    return render(request,'profile.html')


'''
index用関数　企業データを全てindexに返す
'''
def index(request):
    if request.method == 'POST':
        Company_create(request)
        return redirect('rikumane_app:index')
    params = {
        # 'data': Company.objects.all(),
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
    print(request.GET)
    print(request.POST)
    con = int(request.GET.get('id'))
    for one in company_data:
        if one['unique_id'] == con:
            res = one
            break
    if request.GET.get('page_query'):
        page_tag = request.GET.get('page_query')
    else:
        page_tag = ""
    d={
    'data':company_data,
    'title':request.GET.get('name'),
    'start_time':request.GET.get('start_time'),
    'end_time':request.GET.get('end_time'),
    'page':page_tag,
    'company':res,
    }
    if request.GET.get('name') and request.GET.get('start_time') and request.GET.get('end_time'):
        d['start_time'] += ":00"
        d['end_time'] += ":00"
        event = calendar.credentials_account()
        calendar.add_calendar(event,d)

    return render(request,'detail.html',d)


    # 以下、編集部分（吉井）

    # データを変更するものはここで
    if request.method=='POST':
        # データベースを取得
        one = Company.objects.get(pk=request.POST['id'])
        # t:操作するテーブル
        # o:操作内容(Create,Update,Delete)
        t = request.POST['table']
        o = request.POST['operation']
        if t == 'Account':
            if o =='update':
                pass
            elif o =='delete':
                pass
        elif t == 'Company':
            if o =='update':
                pass
            elif o =='delete':
                pass
        elif t == 'Event':
            if o =='create':
                pass
            elif o =='update':
                pass
            elif o =='delete':
                pass
        elif t == 'ES':
            if o =='create':
                pass
            elif o =='update':
                pass
            elif o =='delete':
                pass
        return redirect('rikumane_app:detail')
        
    # データベースを取得
    one = Company.objects.get(pk=request.GET['id'])
    d = {
        company:one,
        event:one.event_set.all(),
        es:one.es_set.all()
    }

    return render(request,'detail.html',d)