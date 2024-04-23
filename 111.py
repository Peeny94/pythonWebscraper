import requests
from bs4 import BeautifulSoup

all_jobs=[]
url = "https://weworkremotely.com/remote-full-time-jobs?"
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
scrape_page(url)