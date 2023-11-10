class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.length*self.breadth
    def perimeter(self):
            return 2*self.length+self.breadth
a=int(input("enter length of rect:"))
b=int(input("enter breadth of rect:"))
obj=Rectangle(a,b)
print("area of rectangle",obj.area())
print("perimeter of rectangle",obj.perimeter())
