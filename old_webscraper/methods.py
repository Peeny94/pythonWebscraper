
name = "lee"

# print(name.capitalize())#python methods.py <- 콘솔창에서 실행해주거나 우측 상단의 디코딩 버튼을 눌러야 실행이 된다. 
 
# list, tuple, dictionary _ 오늘 배울것. 
""" 
리스트일 경우 위와 같은 함수를 활용 가능하나. 배열이 아닌 일반 변수의 경우 불가능하다. 
리스트는 어떠한 속성을 가지는 데이터도 포함이 가능하다. 리스트 안에 리스트도 값으로 넣을 수 있다.
method 는 데이터에 결합된 function
"""
day_of_week =["Mon","Tue","Wed","Thu","Fri"]

# print(day_of_week)
# print(day_of_week.startswith("M"))//ttributeError: 'list' object has no attribute 'startswith'
# print(day_of_week.count("Mon"))//해당 값의 갯수를 표시함
# day_of_week.claer() -완전삭제 day_of_week.remove("Mon") -부분삭제 
# method는 값속성에 따라 쓰임이 한정적이다. function 은 변수값을 설정하여 임의로 기능을 생성한다.
# day_of_week.reverse() //list를 역순으로 재배열 
# day_of_week.append("plus")  
# print((day_of_week.[3]) //배열의 특정위치의 값을 출력 

# print(name.startswith("l"))//True 
# isupper() 값이 전부 대문자일대 boolean값을 출력\\endswith() 끝자리수가 맞는지 확인
# print(name.replace("e","💩")) //l💩💩

days=("Mon","Tue","Wed","Thu","Fri") #tuples은 생성후 데이터 변경이 불가능하다
""" 
print(days[-1])// 배열이므로 호출방법은 [] list 와 동일하다. '-' 는 뒤에서부터 호출한다.

print(days[-1])// Fri -뒤에서부터 호출할땐 1부터 역순이다. -0은 동일하게 'Mon'을 출력한다. 
"""
#  Dicts- 중괄호를 쓰며 key와 value 를 임의로 설정
""" player = {
    'name':['lee'], #list 의 경우 append method를 통해 값을 추가가능
    'age':12,
    'alive':True
    'luv': {
        'name': "poop",
        'fav_food': ["💩"]
    }
}
print(player)
player.pop('age') #해당 key 와 value를 완전 삭제
player['xp'] = 1500
player['name'].append("🗽")
player['luv']['fav_food']
print(player) #특정 key 만 불러올 경우 player.get('key') or player['key'] """

#연습 프로젝드 하기. ch4.5