class Student():
    def __init__(s):
        s.name=0
        s.rno=0
        s.m1=0
        s.m2=0
        s.m3=0
        s.total=s.m1+s.m2+s.m3
        s.avg=s.total/3
    def read(s):
        s.name=input('Enter student name : ')
        s.rno=input('Enter student roll number : ')
        s.m1=float(input('Enter student marks 1 : '))
        s.m2=float(input('Enter student marks 2 : '))
        s.m3=float(input('Enter student marks 3 : '))
    def display(s):
        print(f'\nName : {s.name}\nRoll Number : {s.rno}')
        print(f'Marks 1 : {s.m1}\nMarks 2 : {s.m2}\nMarks 3 : {s.m3}')
        print(f'Total : {s.total}\nAverage : {s.avg}')
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