
from django.db import models

# Create your models here.


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text


class Account(models.Model):
    # UserName
    # Password
    # Email

    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100, unique=True)


class Company(models.Model):
    # URL:企業毎のURL
    # CompanyName:企業名
    # LoginId:ログインのためのID
    # Memo: メモ

    Account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True)
    URL = models.CharField(max_length=200)
    CompanyName = models.CharField(max_length=100)
    LoginId = models.CharField(max_length=100)
    Memo = models.CharField(max_length=500, default='')
    Rate = models.IntegerField(default=0)

    def __str__(self):
        return self.CompanyName

# イベントのテーブル（親テーブル: Company）


class Event(models.Model):
    # Company: そのイベントの属する企業
    # EventName: イベント名
    # EventStart: 開始日時（ex. 2000-01-01 02:11:11+00:00）
    # EventEnd: 終了日時

    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    EventName = models.CharField(max_length=100)
    EventStart = models.DateTimeField()
    EventEnd = models.DateTimeField()
    Flow = models.BooleanField(default=False)
    Complete = models.BooleanField(default=False)

    def __str__(self):
        return self.EventName

# ESのテーブル（親テーブル: Company）


class ES(models.Model):
    # Company: そのイベントの属する企業
    # QuestionTitle: 質問内容
    # TextCounts: 文字数（？）
    # QuestionContents: 質問への回答

    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    QuestionTitle = models.CharField(max_length=100)
    TextCounts = models.IntegerField(default=0)
    QuestionContents = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.QuestionTitle
