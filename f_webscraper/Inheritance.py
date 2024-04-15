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
    
    def rrrrr(self):
        print("stay away!")

class Dog(Ddog):
    def __init__(self, name, breed):
        super().__init__(name, 
                         0.1, 
                         breed
                    )
    
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

print(aDog,bDog) 
