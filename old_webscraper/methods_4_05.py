##install request 모듈을 설치함. terminal에서 pip list 를 통해 확인이 가능하다. 
import keyword
from requests import get
data= ("https://google.com",
       "https://nomadcoders.co",
       "airbnb.com",
       "facebook.com",
       "tiktok.com",
       "nomadcoders.co/python-for-beginners/lectures/3787"
)
################## 다른 방식으로 표현 가능하다._방법1
""" 
for each in data:
    if each.startswith("https://"):
        print("don't have to fix it")
    else:
        print("we have to fix it")
"""
        
#좀 더 간략한 표현 방식_방법2
#보통 출력 변수값을 임의로 지정하나, 데이터와 동일한 값으로 지정. for data in data
""" 
for each in data:
    if not each.startswith("https://"):
        print("have to fix it")
"""

#codeChallenge - 각 응답 코드에 반응하는 loop문을 완성시켜라.
""" 
reference: status_code: 301(new url),302(temperary url),307(temperary),308(permanent) - redirect(300번대 코드는 다른 페이지로 응답한다.)
400,500 - 각각 응답불능(bad Gateway), 오류(Internal Server Error)
"""
results ={} #빈 dictionary를 만듦
for each in data: 
    #print("each의 데이터 값을 알려준다", each)
    if not each.startswith("https://"): #bool
        each = f"http://{each}"#each 변수값에 수정된 값을 넣어 주어야 한다. 
    response = get(each)    
    #print(response) #값 중 하나라도 연결이 오류나면 err. 출력값 확인이 불가능. 단 dicts를 만들어 값을 재입력 후 출력시 오류값을 제외하여 나온다.  
    #print(response.status_code)
        #status_code = str(response.status_code)
    if response.status_code>=200:
        results[each] = "OK" #빈 dicts에 for 문으로 조건값 대입.
    elif response.status_code>=300:
        results[each] = "REDIRECT"
    elif response.status_code>=400:
        results[each] = "Bad_Gateway"
    elif response.status_code>=500:
        results[each] = "Internal_Server_Error"     
    else:
        results[each] ="FAILED"
  
print("\n".join(results)) # \n을 반복문 안에 써줄경우, key값만 출력된다.
""" 
https://google.com
https://nomadcoders.co
http://airbnb.com
http://facebook.com
http://tiktok.com
http://nomadcoders.co/python-for-beginners/lectures/3787
"""
a = set()
for key in results.keys():
    for value in results.values():
        a.add((key,value)) #결과를 set 에 추가한다.
print("\n".join(map(str,a)))
""" 
('https://google.com', 'OK')
('http://facebook.com', 'OK')
('https://nomadcoders.co', 'OK')
('http://airbnb.com', 'OK')
('http://nomadcoders.co/python-for-beginners/lectures/3787', 'OK')
('http://tiktok.com', 'OK')
{'https://google.com': 'OK', 'https://nomadcoders.co': 'OK', 'http://airbnb.com': 'OK', 'http://facebook.com': 'OK', 'http://tiktok.com': 'OK', 'http://nomadcoders.co/python-for-beginners/lectures/3787': 'OK'}
"""
print(results)
""" 
{'https://google.com': 'OK', 'https://nomadcoders.co': 'OK', 'http://airbnb.com': 'OK', 'http://facebook.com': 'OK', 'http://tiktok.com': 'OK', 'http://nomadcoders.co/python-for-beginners/lectures/3787': 'OK'}
"""

for k,v in results.items():
    print("(key={key},value={value})".format(key=k,value=v)) 
""" 
(key=https://nomadcoders.co,value=OK)
(key=http://airbnb.com,value=OK)
(key=http://facebook.com,value=OK)
(key=http://tiktok.com,value=OK)
(key=http://nomadcoders.co/python-for-beginners/lectures/3787,value=OK)
"""