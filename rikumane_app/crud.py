from rikumane_app.models import Company, Account, ES, Event
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


def Account_update(req):
    pass


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
