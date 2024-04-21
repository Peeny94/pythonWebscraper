#객체지향 언어의 필요성
""" 객체의 동일성
class Puppy:
    
    def __init__(self): #__init__(something) <- 무언가 arg를 넣어야 작동.
        print(self) #<__main__.Puppy object at 0x101255af0>
        print("Wow")
aDog = Puppy() # arg 초기화식
print(aDog) #<__main__.Puppy object at 0x101255af0> 
"""

""" class 내 다른 함수 추가한 경우
class Dog:
    
    def __init__(self,name,breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
        
#class 내의 함수에 정의내려진 변수를 끌어올 수 있다. Indent에 주의!!
    def __str__(self):
        return f"Dog named {self.name}, breed:{self.breed}"#Dog named a, breed:beegle Dog named b, breed:Dalmatian
     
        
aDog = Dog(
    name="a",
    breed="beegle"
    )
bDog = Dog(
    name="b",
    breed="Dalmatian"
    )

print(aDog,bDog)  
"""
class Dog:
    
    def __init__(self,name,breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
        
#class 내의 함수에 정의내려진 변수를 끌어올 수 있다. Indent에 주의!!
    def __str__(self):
        return f"Dog named {self.name}, breed:{self.breed}"#Dog named a, breed:beegle Dog named b, breed:Dalmatian
     
        
aDog = Dog(
    name="a",
    breed="beegle"
    )
bDog = Dog(
    name="b",
    breed="Dalmatian"
    )

print(aDog,bDog) 
