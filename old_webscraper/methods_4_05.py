##install request 모듈을 설치함. pip list 를 통해 확인이 가능하다. 
from requests import get
data= ("https://google.com",
       "https://nomadcoders.co/",
       "airbnb.com",
       "facebook.com",
       "tiktok.com",
       "https://nomadcoders.co/python-for-beginners/lectures/3787"
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
results ={} #빈 dictionary를 만듦
for each in data: 
    #print("each의 데이터 값을 알려준다", each)
    if not each.startswith("https://"):
        each = f"http://{each}" #each 변수값에 수정된 값을 넣어 주어야 한다. 
    response = get(each)    
    #print(response) #값 중 하나라도 연결이 오류나면 err. 출력값 확인이 불가능.   
    #print(response.status_code)
    if response.status_code ==200:
        results[each] = "OK" #빈 dicts에 for 문으로 조건값 대입.
    else:
        results[each] ="Failed"
  
print("\n".join(results)) # \n을 반복문 안에 써줄경우

    #if문 내에서 나오는 값은 하기와 같다.
    # print(data,"변수",each)
    # data값은 변동 없이 each에 새로운 값이 저장되어 수정값을 출력.
""" 
    ('1', '2', '3', '4', '5', 'https://6') 변수 http://1
    ('1', '2', '3', '4', '5', 'https://6') 변수 http://2
    ('1', '2', '3', '4', '5', 'https://6') 변수 http://3
    ('1', '2', '3', '4', '5', 'https://6') 변수 http://4
    ('1', '2', '3', '4', '5', 'https://6') 변수 http://5
    ('1', '2', '3', '4', '5', 'https://6') 변수 https://6  
"""
    

