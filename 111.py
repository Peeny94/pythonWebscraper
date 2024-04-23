import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청 오류 확인

        soup = BeautifulSoup(response.content, "html.parser")
        jobs_section = soup.find("section", class_="jobs")
        if jobs_section is None:
            print("섹션을 찾을 수 없습니다.")
            return  # 섹션을 찾지 못했으므로 스크래핑 중단
        
        jobs = jobs_section.find_all("li")[1:-1]
        for job in jobs:
            title = job.find("span", class_="title").text
            company, position, region = job.find_all("span", class_="company")
            url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
            job_data = {
                "title": title,
                "company": company.text,
                "position": position.text,
                "region": region.text,
                "url": f"https://weworkremotely.com{url}",
            }
            all_jobs.append(job_data)
    except requests.RequestException as e:
        print(f"오류 발생: {e}")

# 페이지 수 계산
response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
soup = BeautifulSoup(response.content, "html.parser")
buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))

# 각 페이지 스크래핑
for x in range(buttons):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))
