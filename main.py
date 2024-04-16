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
        #파이썬 언어라 '_'fmf 붙여줘야 한다.
        class_ ="jobs"
    ).find_all("li") 

print(jobs)