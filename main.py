import requests
from bs4 import BeautifulSoup
url ="https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

#print(response.content)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

jobs = soup.find("section",
        #파이썬 언어라 '_'를 붙여줘야 한다.
        class_ ="jobs"
    ).find_all("li")[1:-1] 
for job in jobs:
    title = job.find("span",class_="title").text #'.text': 해당 요소의 실제 텍스트값만 추출
    #region = job.find("span", class_="region").text
    company,position, region  = job.find_all("span", class_="company")
    company= company.text
    position = position.text
    region = region.text
    
    print(title,"\n/",company,"\n/",position,"\n/",region)
    
