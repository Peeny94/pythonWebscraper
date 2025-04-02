import requests
from bs4 import BeautifulSoup
url ="https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

#print(response.content)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

all_jobs=[]
jobs = soup.find("section",
        #파이썬 언어라 '_'를 붙여줘야 한다.
        class_ ="jobs"
    ).find_all("li")[1:-1] #페이지 구성요소에 따라 다르게 설정해준다. 처음과 끝 li태그 정보를 제거.
for job in jobs:
    title = job.find("h4",class_="new-listing__header__title").text #'.text': 해당 요소의 실제 텍스트값만 추출
    #region = job.find("span", class_="region").text // 하기 추출값에 지역이 포함되기 때문에 중복값은 제거.
    #"company"가 포함된 모든 태그를 찾는다. 'find_all' 이용.
    companys = job.find_all("p", class_="new-listing__company-")
    if len(companys) == 3: 
        company,region,position  = companys.text
    elif len(companys) == 0:
        company =[]
        error = "err"
    else :
        continue
    #url 정보 중 특정 태그값의 정보의 다음 요소를 가져올때 'next_sibling["요소"]'를 쓴다.
    #"tooltip" 이라고 쓰면 안나오고 정확한 아이템값을 입력해야 한다. 주의!! company의 경우 find_all을 사용해서 모든 태그를 가져왔기 때문에 문제가 되지 않지만 find의 경우 아이템명이 정확해야만 한다.
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    """
    # 필요없는 부분 'href'를 추출, 두 구성요소에 확신이 있는경우 한번에  가져오도록 한다.
    url = job.find("a")["href"]
    #href 가 없는 경우가 있다고 가정하에 반복문을 통해 href 부분만 부분적으로 추출할 수 있게 한다. 
     <a href=""> 구조일경우
        url = job.find("a")
        if url :
        url = url["href"] 
    
    """
    #dicks 형태로 텍스트값만 키와 값으로 지정.
    job_data ={
        "title": title,
        "company": company,
        "error": error,
        # "position": position.text,
        # "region": region.text,
        "url": f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data) 
    
    print(all_jobs)
    


