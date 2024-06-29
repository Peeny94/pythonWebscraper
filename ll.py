import requests


def acess(r):
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
    print(acess(keywords))
  
acess