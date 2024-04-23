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
        ).find_all("li")[1:-1]
    for job in jobs:
        title = job.find("span",class_="title").text
        company,position,region  = job.find_all("span", class_="company")
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

for x in range(buttons):
    # 리스트에 특성에 따라 페이지 1부터로 임의로 숫자를 변경함.
    url = f"https://weworkremotely.com/remote-full-time-jobs?page=1{x+1}"
    scrape_page(url)
    
print(len(all_jobs))