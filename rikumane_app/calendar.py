import pickle
import os.path
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request   

def credentials_account():
    # カレンダーAPIで操作できる範囲を設定（今回は読み書き）
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    # Google にcalendarへのアクセストークンを要求してcredsに格納します。
    creds = None
    # 有効なトークンをすでに持っているかチェック（２回目以降の実行時に認証を省略するため） 
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # 期限切れのトークンを持っているかチェック（認証を省略するため）
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refrestoken:
            creds.refresh(Request())
        # アクセストークンを要求
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # アクセストークン保存（２回目以降の実行時に認証を省略するため） 
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # カレンダーAPI操作に必要なインスタンス作成
    service = build('calendar', 'v3', credentials=creds)
    # カレンダーAPI操作用インスタンスを返す
    return service

def add_calendar(service,schedule):
    body = {
            # 予定のタイトル
            'summary': schedule['title'],
            # 予定の開始時刻
            'start': {
                'dateTime': schedule['start_time'],
                'timeZone': 'Japan'
            },
            # 予定の終了時刻
            'end': {
                'dateTime': schedule['end_time'],
                'timeZone': 'Japan'
            },
        }
    event = service.events().insert(calendarId='primary',body=body).execute()


def get_event(service,num):
    # 現在時刻を取得
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # カレンダーから予定を取得 
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                         maxResults=num, singleEvents=True,
                                         orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    # 予定があった場合には、出力
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])