class Customer:
    def getdata(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displayCustomer(self):
        print("Customer name:",self.name)
        print("account no:",self.accno)
        print("typeofaccount",self.acctype)
        print("balance",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawl(self,amount):
        if self.balance-amount<0:print("insufficiennt funds")
        else:self.balance=self.balance-amount
ch=0
while ch!=5:
    print("1.new customer")
    print("2.deposit")
    print("3.withdrawl")
    print("4.diplay")
    print("5.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        obj=Customer()
        n=input("enter name:")
        no=int(input("enter accountno:"))
        t=input("enter type of account:")
        b=int(input("enter the amount:"))
        obj.getdata(n,no,t,b)
    if ch==2:
        b=int(input("enter the amount to be deposited:"))
        obj.deposit(b)
    if ch==3:
        c=int(input("enter the amount to be withdraw:"))
        obj.withdrawl(b)
    if ch==4:
        obj.displayCustomer()  
    else:print("program terminated...")
        
    
    
        

