#객체지향 언어의 필요성
""" 객체의 동일성
class Puppy:
    
    def __init__(self): #__init__(something) <- 무언가 arg를 넣어야 작동.
        print(self) #<__main__.Puppy object at 0x101255af0>
        print("Wow")
aDog = Puppy() # arg 초기화식
print(aDog) #<__main__.Puppy object at 0x101255af0> 
"""

class Dog:
    
    def __init__(self):
        self.name = "Ruffus"
        
        
aDog= Dog() 
print(aDog.name) 