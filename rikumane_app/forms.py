from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')

class CompanyForm(forms.Form):
    # company_data:id(自動),URL,Company
    # 
    URL = forms.CharField(max_length=200)
    CompanyName = forms.CharField(max_length=200,required=False)
    LoginId = forms.CharField(max_length=200,required=False)
    Memo = forms.CharField(max_length=200,required=False)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     url = cleaned_data['CompanyName']
    #     print('url:',url)
    #     if not url:
    #         print('url error')
    #         raise forms.ValidationError('errorrrrr')
    #     return cleaned_data

class EventDataForm(forms.Form):
    EventName = forms.CharField(
            label='イベント名',
            required = True,
    )
    EventStart = forms.DateTimeField(
        label='開始日時',
        required=True,
    )
    EventEnd = forms.DateTimeField(
        label='終了日時',
        required=True,
    )
    