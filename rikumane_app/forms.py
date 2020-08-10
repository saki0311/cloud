from django import forms

class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')

# class CompanyDataForm(forms.Form):
#     # company_data:id(自動),URL,Company
#     # 
#     URL = forms.CharField(
#         label='URL',
#         required=True,
#         )
#     Company = forms.CharField(
#         label='企業名',
#         required = True,
#         )

# class EventDataForm(forms.Form):
#     # 
#     # 

#     EventName = forms.CharField(
#         label='イベント名',
#         required = True,
#         )
#     EventStart = forms.DateTimeField(
#         label='開始日時',
#         required=True,
#     )
    
#     EventEnd = forms.DateTimeField(
#         label='終了日時',
#         required=True,
#     )
    