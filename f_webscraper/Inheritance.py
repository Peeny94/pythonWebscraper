class Ddog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def sleep(self):
        print("zzz")

class GuardDog(Ddog):
    def __init__(self, name, breed):
        super().__init__(name, 
                         5, 
                         breed
                    )
        self.aggresive = True  
    
    def rrrrr(self):
        print("stay away!")

class Dog(Ddog):
    def __init__(self, name, breed):
        super().__init__(name, 
                         0.1, 
                         breed
                    )
        self.spoiled =True #독자적인 property를 생성할 수있다.
    
    def woof_woof(self):
        print("Inheritance!") 
        
aDog = Dog(
    name="a",
    breed="beegle"
    )
bDog = Dog(
    name="b",
    breed="Dalmatian"
    )

bDog.sleep() 
