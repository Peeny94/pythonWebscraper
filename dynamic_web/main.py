from playwright.sync_api import sync_playwright #sync를 적는 것은 playwright 을 작동시키는 다른 방식이 있어서라고함. 다양한 브라우저를 병렬식으로 작동시키는 건 어렵고 다른 쉬운 걸 이번 강의에서 다룸.

p = sync_playwright().start() # 클래스 인스턴스화 , 초기화 
# 브라우저 만들기. 
browser = p.chromium.launch(headless=False) # 브라우저 초기화

page = browser.new_page() # 브라우저 탭 생성
page.goto("https://www.google.com/") # url로 이동함
page.screenshot(path ="screenshot.png") # headless mode 에선 브라우저가 실행되지만 playwright 가 기본적으로 브라우저를 보여주지 않기때문에(headless =True) 임의로 코드를 실행됨을 확인하기 위한 메소드.