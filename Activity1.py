class cat:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f"I am a cat my nameis {self.name} and my age is {self.age}")

    def makesound(self):
        print("Meow")

class dog:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f"I am a dog my name is {self.name} and my age is {self.age}")

    def makesound(self):
        print("Bark")

class tiger:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f"I am a tiger my nameis {self.name} and my age is {self.age}")

    def makesound(self):
        print("Roar")

cat1=cat("Lily" , 3)
dog1=dog("tom" , 2)
tiger1=tiger("Remy" , 6)

for i in (cat1 , dog1 , tiger1):
    i.makesound()
    i.info()