import requests
from bs4 import BeautifulSoup
import logging # 웹페이지에서 지정된 값 이외에 변수를 처리하기 위한 목적
import time  # 요청 간 딜레이 추가
# 기존 코드 중 self 호출로 초기화 식을 좀 더 많이 씀. --> 코드 가독성 향상에 좋은듯. 
# https://remoteok.com/remote-{x}-jobs RemotOk site scraping project.
class Scrape:

    def __init__(self,url):

        response = requests.get(url)
        self.soup = BeautifulSoup(
            response.content,
            "html.parser"
        )
        #이상한 코딩. 기본 이론이 부족한것임. self.url = soup
    def scrape_page(self): 
        # self.soup 로 바꿔줌 . 정의내리는 것과는 별개로 함수 호출 방식을 헷갈리고 있음. 공부하자.
        jobs = self.soup.find("section",
                class_ ="jobs"
            ).find_all("li")[:-1]
        all_jobs= []

        for job in jobs:
            title = job.find("span",class_="title").text
            companys = job.find_all("span", class_="company")   
            if len(companys) == 3: 
                company,position,region  = companys
            elif len(companys) == 2:
                company,position = companys
                region= None
            else :
                continue
            """         else:
                for err in companys:
                    logging.warning(f"errURL: {url}")              
                # for err_info in companys:
                #     logging.warning(f"errURL: {url}\n errVelue: {companys}")  # 로그 기록
                continue # 다음 job으로 이동 
                """
            url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
            job_data ={     
                "title": title,
                "company": company.text,
                "position": position.text,
                "region": region.text,
                "url": f"https://remoteok.com/remote-{url}-jobs",
            }
            #Scrape(url).scrape_page를 append() 하니까 함수 객체가 리스트에 추가됨.
            # 대신, scraper() 실행 결과를 리스트에 추가해야 함.
            all_jobs.extend(scraper())
            # 메소드를 돌리고 결과값 정의를 안함. 정말 바보같다. 
        return all_jobs
class Category:
    # self 정의는 중요하다. 정적 메소드란 걸 표기, 클래스 내에서만 실행됨. ...자바이론?     ---나중에 한 번 더 check. 
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

    def get_pages(self):    
        response =requests.get(self.url, headers=self.headers)
        
        if response.status_code == 403:
            print("Access Denied (403). Trying again after a short delay...")
            time.sleep(5)  # 5초 대기 후 다시 시도
            response = requests.get(self.url, headers=self.headers)
        
        elif response.status_code != 200:
            print(f"Failed to access {self.url} - Status Code: {response.status_code}")
            return []  # 페이지 개수를 1로 가정 (예외 처리)
        
        soup = BeautifulSoup(response.content, "html.parser")
        #키워드 목록으로  "remotelOk" 사이트에서 해당 키워드로 일자리 검색하기
        keywords = ["flutter","python","golang"]
        page= soup.find("div", class_="page").find("table").next_sibling["today"]
        buttons =  len(keywords) #page 양을 통해 반복문 횟수를 결정한다.
        return buttons

for x in keywords:
        
    #로컬에서 웹서버에 접속시도시 
    # r = requests.get("https://remoteok.com/remote-{keywords}-jobs",)
    # print(r.status_code)# 503
    # print(r.content)

    # """ 사이트 차단됨: code 503, 웹 개발자 - 네트워크에서 새로고침 - 서버로 브라우저가 requests 한 정보를 확인한다. :remote-flutter-jobs(code: 200)Header ->Request Header
    # ->User-Agent:
    #  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
    # """

    # 웹에서 사이트에 접속시도하는 것처럼 해당 사이트의 header정보로 접속시도시
    r = requests.get(f"https://remoteok.com/remote-{x}-jobs")
    # https://remoteok.com/remote-{키워드}-jobs 
    # def 함수로 만들되, class로 변형도 시켜보자: 모든 일자리 정보를 class 에 넣고 method를 활용해서 job들을 배열안에 넣어보자.
    # OOP형태로의 변환도 시도해봐라.
    if r.status_code ==200:
       print(f"Successfully accessed {url}")
    else:
        print(f"Failed to access {url} - Status Code: {r.status_code}")