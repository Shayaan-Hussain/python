class Student():
    def __init__(self):
        self.name=0
        self.rno=0
        self.m1=0
        self.m2=0
        self.m3=0
    def read(self):
        self.name=input('Enter student name : ')
        self.rno=input('Enter student roll number : ')
        self.m1=float(input('Enter student marks 1 : '))
        self.m2=float(input('Enter student marks 2 : '))
        self.m3=float(input('Enter student marks 3 : '))
        self.total=self.m1+self.m2+self.m3
        self.avg=self.total/3
    def display(self):
        print(f'\nName : {self.name}\nRoll Number : {self.rno}')
        print(f'Marks 1 : {self.m1}\nMarks 2 : {self.m2}\nMarks 3 : {self.m3}')
        print(f'Total : {self.total}\nAverage : {self.avg}')
studlist=[]
n=int(input('Enter number of students : '))
for i in range(0,n):
    stud=Student()
    print(f'Enter student {i+1} data')
    stud.read()
    studlist.append(stud)
print('Student data:')
for i in range(0,n):
    stud=studlist[i]
    stud.display()