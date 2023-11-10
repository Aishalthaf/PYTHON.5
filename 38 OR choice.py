class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area=", self.length*self.breadth)
    def perimeter(self):
        print("perimeter=", 2*self.length+self.breadth)
a=Rectangle(3,5)
print("enter choice 1 or 2")
ch=int(input("enter the choice"))
if(ch==1):
 a.area()
elif(ch==2):
 a.perimeter()
else:
 print("wrong choice")
