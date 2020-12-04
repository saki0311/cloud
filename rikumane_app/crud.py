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
    company = Company(
        Account=account,
        URL=req.POST['URL'],
        CompanyName=req.POST['CompanyName'],
        LoginId=req.POST['LoginId'],
        Rate=req.POST.get('want'),
        Category=req.POST.get('category')
    )
    company.save()


def Company_update(req, account):
    data = Company.objects.get(Account_id=account.id,id=req.POST.get('id'))
    data.URL=req.POST.get('URL')
    data.CompanyName=req.POST.get('CompanyName')
    data.LoginId=req.POST.get('LoginId')
    data.Rate=req.POST.get('want')
    data.Category=req.POST.get('category')
    data.save()


def Company_delete(req,account):
    data = Company.objects.get(Account_id=account.id,id=req.POST.get('id'))
    data.delete()

# AccountのCRUD


def Account_create(req):
    pass

def Account_update(req):
    user = User.objects.get(id=req.user.id)
    user.username = req.POST.get("edit-user")
    user.first_name = req.POST.get("edit-firstname")
    user.last_name = req.POST.get("edit-lastname")
    user.email = req.POST.get("edit-mail")
    user.save()


    
def CommonInfo_update(req,account):
    user = User.objects.get(id=account.id)
    com_info = CommonInfo.objects.get(id=account.id)
    com_info.MemoES = req.POST.get('entrysheet')
    com_info.MemoAnalysis = req.POST.get('self_analysis')
    com_info.Memo = req.POST.get('memo')
    com_info.save()

def Account_delete(data):
    data.delete()

def Company_data_update(req):
    user = req.user
    company_memo = req.POST.get('memo')
    company_es = req.POST.get('ES')
    
    company = Company.objects.get(Account_id=user.id,id=req.POST.get('com_id'))
    company.Memo = company_memo
    company.ES = company_es
    company.save()

# ESのCRUD


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
