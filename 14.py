import requests
from bs4 import BeautifulSoup
import logging # 웹페이지에서 지정된 값 이외에 변수를 처리하기 위한 목적

""" @@@@@ 코드챌린지_04 @@@@@
berlinstartupjobs.com 웹사이트용 스크래퍼를 만듭니다.
스크래퍼는 다음 URL을 스크랩할 수 있어야 합니다:
https://berlinstartupjobs.com/engineering/
https://berlinstartupjobs.com/skill-areas/python/
https://berlinstartupjobs.com/skill-areas/typescript/
https://berlinstartupjobs.com/skill-areas/javascript/
첫 번째 URL에는 페이지가 있으므로 pagination 을 처리해야 합니다.
나머지 URL은 특정 스킬에 대한 것입니다. URL의 구조에 스킬 이름이 있으므로 모든 스킬을 스크래핑할 수 있는 스크래퍼를 만드세요.
회사 이름, 직무 제목, 설명 및 직무 링크를 추출하세요. 

"""


class Scrape:
    all_jobs= []
    def __init__(self,url):

        response = requests.get(url)
        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )
        self.url = soup
        
# 직무제목,회사이름, 직무링크, 설명
# bjs-jild__h https://berlinstartupjobs.com/engineering/senior-golang-engineer-f-m-d-berlin-hybrid-fincompare/
# bjs-jlid__b https://berlinstartupjobs.com/companies/fincompare/
# links-box    bjs-bl bjs-bl-whisper # 구직명
# bjs-jlid__description

    def scrape_page(self,soup,all_jobs): 

        jobs = soup.find("li",
                class_ ="bjs-jild"
            ).find_all("li") # [:-1]
        for job in jobs:
            title = job.find("h4",class_="bjs-jild__h").text
            company= job.find("a", class_="bjs-jlid__b").text   
            description = job.find("div", class_="bjs-jlid__description").text
            url = job.find_all("div", class_="links-box").next_sibling["a"]
            job_data ={     
                "title": title,
                "company": company.text,
                "description": description.text,
                "url": f"https://berlinstartupjobs.com/skill-areas/{url}",
            }
            all_jobs.append(job_data)
class Pagination:
          
    def get_pages(url):    
        response =requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        #class 는 class 메서드와의 구별을 위헤 '_'를 붙여서 사용한다. 그 외 기능은 없다. '_'를 붙이지 않으면 구문에 오류가 난다.
        buttons =  len(soup.find("ul", class_="bsj-now").find_all("a", class_="page-numbers")) #page 양을 통해 반복문 횟수를 결정한다.
        return buttons
    totla_pages = get_pages("https://berlinstartupjobs.com/engineering/page/1/")
    #scrap_page에서 따로 url 을 정의하지 않는 건 하기 반복문으로 전체 페이징 코드를 작성하기 때문.
    for x in range(totla_pages):
        # 리스트에 특성에 따라 페이지 1부터로 임의로 숫자를 변경함.
        url = f"https://berlinstartupjobs.com/engineering/page/{x+1}/"
        #scrape_page(url)

    # print(len(all_jobs))
    # print(all_jobs)

    #키워드 목록으로  "remotelOk" 사이트에서 해당 키워드로 일자리 검색하기

    keywords = [
        "python",
        "typescript",
        "javascript",
    ]
    #로컬에서 웹서버에 접속시도시 
    r = requests.get("https://berlinstartupjobs.com/skill-areas/{keywords}",
    )
    # print(r.status_code)# 503
    # print(r.content)

    # 웹에서 사이트에 접속시도하는 것처럼 해당 사이트의 header정보로 접속시도시
    r = requests.get("https://berlinstartupjobs.com/skill-areas/{keywords}", headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    )
    # https://remoteok.com/remote-{키워드}-jobs 
    # def 함수로 만들되, class로 변형도 시켜보자: 모든 일자리 정보를 class 에 넣고 method를 활용해서 job들을 배열안에 넣어보자.
    # OOP형태로의 변환도 시도해봐라. 💩

    print(r.content)