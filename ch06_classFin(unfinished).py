import requests
from bs4 import BeautifulSoup
import logging # 웹페이지에서 지정된 값 이외에 변수를 처리하기 위한 목적

class Scrape:
    all_jobs= []
    def __init__(self,url):

        response = requests.get(url)
        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )
        self.url = soup
    def scrape_page(self,soup,all_jobs): 

        jobs = soup.find("section",
                class_ ="jobs"
            ).find_all("li")[:-1]
        for job in jobs:
            title = job.find("span",class_="title").text
            companys = job.find_all("span", class_="company")   
            if len(companys) == 3: 
                company,position,region  = companys
            elif len(companys) == 2:
                company,position = companys
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
                "url": f"https://weworkremotely.com{url}",
            }
            all_jobs.append(job_data)
class Pagination:
          
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
        #scrape_page(url)

    # print(len(all_jobs))
    # print(all_jobs)

    #키워드 목록으로  "remotelOk" 사이트에서 해당 키워드로 일자리 검색하기

    keywords = [
        "flutter",
        "python",
        "golang"
    ]
    for x in len(keywords):
        
        #로컬에서 웹서버에 접속시도시 
        r = requests.get("https://remoteok.com/remote-{keywords[x]}-jobs",
        )
        # print(r.status_code)# 503
        # print(r.content)

        """ 사이트 차단됨: code 503, 웹 개발자 - 네트워크에서 새로고침 - 서버로 브라우저가 requests 한 정보를 확인한다. :remote-flutter-jobs(code: 200)Header ->Request Header
        ->User-Agent:
            Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
        """
        # 웹에서 사이트에 접속시도하는 것처럼 해당 사이트의 header정보로 접속시도시
        r = requests.get("https://remoteok.com/remote-{keywords[x]}-jobs", headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        )
        # https://remoteok.com/remote-{키워드}-jobs 
        # def 함수로 만들되, class로 변형도 시켜보자: 모든 일자리 정보를 class 에 넣고 method를 활용해서 job들을 배열안에 넣어보자.
        # OOP형태로의 변환도 시도해봐라.
        remote = Scrape(url)
    p   print(all_jobs)
