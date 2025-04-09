import requests
from bs4 import BeautifulSoup
import logging # 웹페이지에서 지정된 값 이외에 변수를 처리하기 위한 목적
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time

all_jobs=[]
def scrape_page(url): 

    response = requests.get(url)

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )
    jobs = soup.find("section",
            class_ ="jobs"
        ).find_all("li")[:-1]
    print(len(jobs))
    for job in jobs:
        title = job.find("h4",class_="new-listing__header__title").text
        company = "N/A"
        headquarter = "N/A"
        company_info = job.find("div", class_="new-listing paid-logo")
        if company_info:
            companys = company_info.find_all("p")
            for comp in companys:
                # class가 없을 경우에도 빈 배열을 출력하게 됨.
                if "new-listing__company-name" in comp.get("class", []): 
                    company = comp.text.strip()
                elif "new-listing__company-headquarters" in comp.get("class", []):
                    headquarter = comp.text.strip()
        # print(company.prettify())  --> 전체html 이 나옴 정제가 안됨. 
        # strip은 양끝쪽에 있는 공백과 특수문자 제거와 지정한 문자제거,
        # strip(" \r") 한칸 제거 : (\n)과 같은 기능
        # location = location.contents[0].strip()
        location = job.find("div",class_="new-listing__categories")
        if location:
             # recursive은 같은 클래스명을 전부 가져오는것을 방지 가장 위에 있는것만 가져오기
             #text --> string 으로 사용함. soup 4.12 이후.
            loc = location.find(string=True, recursive=False)
            if loc:
                loc = loc.strip() # 공백 제거.
            else:
                #cancel 텍스트 중 아이콘 제거하기. 
                location = ''.join(list(location.stripped_strings)[:-1])
        else:
            location = "N/A"
            logging.warning("Location N/A")
            continue 
        # positions = job.find("p", class_="new-listing__categories__category").text
        # url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"] 이 한줄을 하기의 코드로 써서 해봄.
        job_url_tag = job.find("div", class_="tooltip--flag-logo")
        if job_url_tag and job_url_tag.next_sibling and job_url_tag.next_sibling.get("href"):
            url = job_url_tag.next_sibling["href"]
        else:
            url = "#"  
        today = datetime.today().strftime('%Y-%m-%d')
        # "date":{today} ->  "date" 필드가 문자열이 아닌 set 타입 으로 저장 
        # set(["2024-04-09"])     
        job_data ={  
            "date":today,    
            "title": title,
            "company": company.strip(),
            "headquarter": headquarter.strip(),
            "location": location,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)
        
def get_pages(url):    
    response =requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons =  len(soup.find("div", class_="pagination").find_all("span", class_="page")) #page 양을 통해 반복문 횟수를 결정한다.
    return buttons
totla_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")
#scrap_page에서 따로 url 을 정의하지 않는 건 하기 반복문으로 전체 페이징 코드를 작성하기 때문.
for x in range(totla_pages):
    # 리스트에 특성에 따라 페이지 1부터로 임의로 숫자를 변경함.
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))
print(all_jobs)

# 인증
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# 구글 시트 열기 (시트 이름 필요)
# sheet = client.open("web_site").sheet1
#gspread의 Spreadsheet 객체에 존재하는 worksheet 메소드를 사용하는 것이므로 객체명 임의 지정 안됨. 존재하는 메소드를 사용하는 것! 
spreadsheet = client.open("web_site")  # 시트 파일 이름
# sheet = spreadsheet.worksheet("wework")  # 워크시트 탭 임의 지정은 안됨. 탭은 생성해놔야봄.
# 기존에 동일한 이름이 있다면 에러가 나므로 try-except 사용 권장
try:
    # sheet_name = f"Wework_{today}"
    sheet = spreadsheet.add_worksheet(title="wework", rows="100", cols="20")
except gspread.exceptions.APIError:
    # 이미 존재하는 경우 해당 시트를 그대로 씀.
    sheet = spreadsheet.worksheet("wework")
    sheet.clear()  # 이전 내용 지우기 (선택사항) --헤더보다 앞에있어야 시트전체 삭제로 1행의 헤더가 삭제되지 않게 됨. 주의!
# 헤더 작성 //sheet.append_row(["Date","Title", "Company", "Headquarter", "Location", "URL"])
header = ["Date", "Title", "Company", "Headquarter", "Location", "URL"]

# 시트의 첫 번째 행 확인
existing_header = sheet.row_values(1)

# 헤더가 없거나 다를 경우만 추가
if existing_header != header:
    sheet.insert_row(header, 1)  # 1번 행에 삽입

# 데이터 쓰기
# for job in all_jobs:
#     sheet.append_row([
#         job["date"],
#         job["title"],
#         job["company"],
#         job["headquarter"],
#         job["location"],
#         job["url"]
#     ])
#     time.sleep(1)  # 1초 대기 (1분에 약 60건)
values = []
for job in all_jobs:
    values.append([
        job["date"],
        job["title"],
        job["company"],
        job["headquarter"],
        job["location"],
        job["url"]
    ])
# 한 번에 전체 데이터 전송 (매우 빠르고 안정적)
#  데이터 삽입시 데이터 타입이 문자열 또는 숫자로 동일하여야 api 전송 됨.
sheet.append_rows(values)