import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 인증
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# 구글 시트 열기 (시트 이름 필요)
sheet = client.open("My Job Scraping Data").sheet1

# 헤더 작성
sheet.append_row(["Title", "Company", "Headquarter", "Location", "URL"])

# 데이터 쓰기
for job in all_jobs:
    sheet.append_row([
        job["title"],
        job["company"],
        job["headquarter"],
        job["location"],
        job["url"]
    ])