import requests
from bs4 import BeautifulSoup

all_jobs=[]
def scrape_page(url): 

    response = requests.get(url)

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )
    jobs = soup.find("section",
            class_ ="jobs"
        ).find_all("li")[1:-2]
    for job in jobs:
        title = job.find("span",class_="title").text
        companys = job.find_all("span", class_="company")
        if len(companys) >= 3: 
            company,position,region  = companys
        else:
            company,position = companys
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        job_data ={     
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data) 
        
response =requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")

soup = BeautifulSoup(response.content, "html.parser")

buttons =  len(soup.find("div", class_="pagination").find_all("span", class_="page")) #page 양을 통해 반복문 횟수를 결정한다.

#scrap_page에서 따로 url 을 정의하지 않는 건 하기 반복문으로 전체 페이징 코드를 작성하기 때문.
for x in range(buttons):
    # 리스트에 특성에 따라 페이지 1부터로 임의로 숫자를 변경함.
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))