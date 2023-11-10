class Student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name= name
        self.course= course
    def displayStudent(self):
        print("rollno:",self.rollno)
        print("name:",self.name)
        print("course:",self.course)
stud1=Student(10,"malu","MCA")
stud2=Student(11,"anu","MCA")
stud1.displayStudent()
stud2.displayStudent()
