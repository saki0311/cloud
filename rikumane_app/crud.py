from rikumane_app.models import Company, CommonInfo, ES, Event
from django.contrib.auth.models import User

'''
データベースの操作全般を担う
共通の引数：viewに送信されたリクエスト
***_create:データを生成
***_update:データを更新
***_delete:データを削除
'''

# CompanyのCRUD
def Company_create(req, account):
    Company(
        Account=account,
        URL=req.POST['URL'],
        CompanyName=req.POST['CompanyName'],
        LoginId=req.POST['LoginId'],
        Rate=req.POST.get('want'),
        Category=req.POST.get('category')
    ).save()


def Company_update(req, data):
    data.URL=req.POST['URL']
    data.CompanyName=req.POST['CompanyName']
    data.LoginId=req.POST['LoginId']
    data.save()


def Company_delete(data):
    data.delete()

# AccountのCRUD


def Account_create(req):
    pass

def CommonInfo_update(req,account):
    user = User.objects.get(id=account.id)
    com_info = CommonInfo.objects.get(id=account.id)
    com_info.MemoES = req.POST.get('entrysheet')
    com_info.MemoAnalysis = req.POST.get('self_analysis')
    com_info.Memo = req.POST.get('memo')
    com_info.save()

def Account_delete(data):
    data.delete()

# ESのCRUD


def ES_create(req):
    pass


def ES_update(req):
    pass


def ES_delete(data):
    data.delete()

# EventのCRUD


def Event_create(req):
    pass


def Event_update(req):
    pass


def Event_delete(data):
    data.delete()
