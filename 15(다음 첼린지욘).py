# Flask를 사용해 잡 스크래퍼의 프론트엔드를 구축합니다.
# 유저는 python, javascript, java 등과 같은 용어를 검색할 수 있어야 합니다.
# 스크래퍼는 berlinstartupjobs.com, weworkremotely.com 및 web3.career의 결과를 표시해야 합니다.
# 우리는 이미 berlinstartupjobs.com 스크래퍼에 대한 코드가 있으므로 weworkremotely.com 및 web3.career를 스크래핑하는 코드를 작성해야 합니다.
# 검색 URL은 다음과 같습니다:
# https://berlinstartupjobs.com/skill-areas// where <s> is the search term (i.e https://berlinstartupjobs.com/skill-areas/python/)
# https://web3.career/-jobs where <s> is the search term (i.e https://web3.career/python-jobs)
# https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term= where <s> is the search term (i.e https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python)


from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

"""
Do this when scraping a website to avoid getting blocked.

headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept':
      'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
}

response = requests.get(URL, headers=headers)
"""


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()


