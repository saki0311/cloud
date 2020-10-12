
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Company(models.Model):
    # URL:企業毎のURL
    # CompanyName:企業名
    # LoginId:ログインのためのID

    URL = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    LoginId = models.CharField(max_length=100)
    def __str__(self):
        return '<企業名：{0}>'.format(self.CompanyName)

class Event(models.Model):
    # Company:そのイベントの属する企業
    # EventName:イベント名
    # EventStart:開始日時（ex. 2000-01-01 02:11:11+00:00）
    # EventEnd:終了日時
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    EventName = models.CharField(max_length=100)
    EventStart = models.DateTimeField()
    EventEnd = models.DateTimeField()
    def __str__(self):
        return '<{0}>'.format(self.EventName)