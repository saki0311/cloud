
from django.db import models
from django.contrib.auth import get_user_model


class CommonInfo(models.Model):
    '''
    UserName:なまえ\n
    Password:パスワード\n
    Email:メアド\n
    Image:画像（証明写真など）\n
    Memo(ESと自己分析でそれぞれ)\n
    '''

    Account = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    Image = models.ImageField(upload_to='files/',null=True)
    MemoAnalysis = models.CharField(max_length=4096,default='')
    MemoES = models.CharField(max_length=4096,default='')
    Memo = models.CharField(max_length=4096,default='')


class Company(models.Model):
    '''
    Account:属するアカウント\n
    URL:企業毎のURL\n
    CompanyName:企業名\n
    LoginId:ログインのためのID\n
    Memo: メモ\n
    Rate:志望度\n
    category：カテゴリ\n
    '''

    Account = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True)
    URL = models.CharField(max_length=200)
    CompanyName = models.CharField(max_length=100)
    LoginId = models.CharField(max_length=100)
    Memo = models.CharField(max_length=500, default='')
    Category = models.CharField(max_length=500)
    Rate = models.IntegerField(default=0)
    ES = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.CompanyName


class Event(models.Model):
    '''
    Company: そのイベントの属する企業\n
    EventName: イベント名\n
    EventStart: 開始日時（ex. 2000-01-01 02:11:11+00:00）\n
    EventEnd: 終了日時\n
    Flow:選考フローにも載せるか\n
    Complete:そのイベントが完了したかどうか\n
    Address:住所\n
    '''

    Company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    EventName = models.CharField(max_length=100)
    EventStart = models.DateTimeField()
    EventEnd = models.DateTimeField()
    Flow = models.BooleanField(default=False)
    Complete = models.BooleanField(default=True)
    Address = models.CharField(max_length=200,default='')
    Description = models.CharField(max_length=1024)

    def __str__(self):
        return self.EventName

class ES(models.Model):
    '''
    Company: そのイベントの属する企業\n
    QuestionTitle: 質問内容\n
    TextCounts: 文字数（？）\n
    QuestionContents: 質問への回答\n
    '''
    Company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    QuestionTitle = models.CharField(max_length=100)
    TextCounts = models.IntegerField(default=0)
    QuestionContents = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.QuestionTitle
