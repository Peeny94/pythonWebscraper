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
page.goto("https://www.wanted.co.kr/") # url로 이동함
time.sleep(4)
# Aside_searchButton__Ib5Dn Aside_isNotMobileDevice__ko_mZ 에서 중간 띄어쓰기 된 부분은 그 하위 명칭(추정, 카카오톡 클론에서 자세한 css를 배울 수 있음)
# css selector 메소드를 사용, 클래스 명을 가져와서 그 요소(element)를 click 하는 기능을 넣을 수 있음.
# page.locator("button.Aside_searchButton__Ib5Dn").click() : click 메소드와 동일한 방식과 기능
page.click("button.Aside_searchButton__Ib5Dn") #class 명이 변경될 경우 get_by_"요소명" 으로 해당 element 를 가져올 수 있다. 
time.sleep(4)
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(4)
# keyboard.down 을 통해 임의의 입력신호를 보냄
page.keyboard.down("Enter")
time.sleep(4)
# 포지션을 클릭 주의!!!!!해당 태그가 클릭시 링크로 이동해야 하기 때문에 a태그의 id 값을 가져와서 해당 링크를 클릭해야함. a#은 처음 보는 코드. 추후 보강 요
page.click("a#search_tab_position")
time.sleep(10)
page.keyboard.down("End")
time.sleep(5)
page.keyboard.down("End")
time.sleep(5)
page.keyboard.down("End")
time.sleep(5)
page.keyboard.down("End")
time.sleep(5)
p.stop()
