class square:
    def __init__(self , side):
        self.side=side
    def area(self):
        print(f"The area is {self.side*self.side}")

class circle:
    def __init__(self , radius):
        self.radius=radius
    def area(self):
        print(f"the area is {self.radius*self.radius*3.14}")

class rectangle:
    def __init__(self , length , breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"The area is {self.length*self.breadth}")

obj1=square(5)
obj2=circle(3)
obj3=rectangle(7)

for i in (obj1 , obj2 , obj3):
    i.area()
        