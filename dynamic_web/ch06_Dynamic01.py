from playwright.sync_api import sync_playwright #sync를 적는 것은 playwright 을 작동시키는 다른 방식이 있어서라고함. 다양한 브라우저를 병렬식으로 작동시키는 건 어렵고 다른 쉬운 걸 이번 강의에서 다룸.
import time

p = sync_playwright().start() # 클래스 인스턴스화 , 초기화 
'''
# 브라우저 만들기. 
1단계: find URL, 2step: input Keyword and pressing ENTER key and await 5sec, 3step: find category, 4step: scroll Page(3 times)
'''
##screenshot, lunch 메소드는 많은 argue 를 가질 수 있음. aruge 자체를 집어넣을 경우 해당 argue가 필수적일 경우가 많고, 변수에 저장된 다양한 타입의 argue는 옵션.
browser = p.chromium.launch(headless=False) # 브라우저 초기화

page = browser.new_page() # 브라우저 탭 생성
page.goto("https://www.google.com/") # url로 이동함
page.screenshot(path ="screenshot.png") # headless mode 에선 브라우저가 실행되지만 playwright 가 기본적으로 브라우저를 보여주지 않기때문에(headless =True) 임의로 코드를 실행됨을 확인하기 위한 메소드.

def plus(a,b):
    return a+b
# argue 지정시에 첫번째가 객체에 값을 집어넣는 형태라면, 뒤에 따라오는 배열값을 객체지정 없이 넣을 수 없음. 중요!
plus(1,2)