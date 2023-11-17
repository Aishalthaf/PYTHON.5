class Cars:
    def __init__(self,color,price,kilometer):
        self.color=color
        self.price=price
        self.kilometer=kilometer
    def __len__(self):
        return self.kilometer
    def __add__(self,other):
        return self.price+other.price
car1=Cars("red",200000,5000)
car2=Cars("black",500000,5200)
print(len(car1))
print(len(car2))
print(car1+car2)

