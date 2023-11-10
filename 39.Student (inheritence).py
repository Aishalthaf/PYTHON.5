class Student:
    def getdata(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def displayStudent(self):
        print ("name",self.name)
        print ("rollno",self.rollno)
        print ("course",self.course)
        
class Test(Student):
    def getmark(self,marks):
        self.marks=marks
    def displayTest(self):
        print("marks",self.marks)
r=input("enter the name:")
n=int(input("enter the rollno:"))
c=input("enter the course:")
m=int(input("enter the marks:"))
stud1=Test()
stud1.getdata(r,n,c)
stud1.getmark(m)
stud1.displayStudent()
stud1.displayTest()
