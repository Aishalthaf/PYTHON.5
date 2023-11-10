class Cars:
    def __init__(self,name,prize,color):
        self.name=name
        self.prize=prize
        self.color=color
    def displayCars(self):
         print("name:",self.name)
         print("prize:",self.prize)
         print("color:",self.color)
car1=Cars("porsche",2.45,"red")
car2=Cars("thar",3.45,"black")
car1.displayCars()
car2.displayCars()
