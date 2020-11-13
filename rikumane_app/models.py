
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

'''
# ユーザモデルのカスタマイズ
class AccountUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have a email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class AccountUser(AbstractBaseUser):
    email = models.EmailField(max_length=128, unique=True)
    Image = models.ImageField(upload_to='files/',null=True)
    MemoAnalysis = models.CharField(max_length=1000,default='')
    MemoES = models.CharField(max_length=1000,default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
'''


class Company(models.Model):
    '''
    Account:属するアカウント\n
    URL:企業毎のURL\n
    CompanyName:企業名\n
    LoginId:ログインのためのID\n
    Memo: メモ\n
    Rate:志望度\n
    Category:カテゴリ\n
    '''

    Account = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    URL = models.CharField(max_length=200)
    CompanyName = models.CharField(max_length=100)
    LoginId = models.CharField(max_length=100)
    Memo = models.CharField(max_length=500, default='')
    Rate = models.IntegerField(default=0)
    Category = models.CharField(max_length=100,default='')

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
    Flow = models.BooleanField(default=True)
    Complete = models.BooleanField(default=False)
    Address = models.CharField(max_length=200,default='')

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
