class Employee():
    def __init__(e):
        e.code=0
        e.year=0
        e.name=0
    def read(e):
        e.code=int(input('Enter employee code : '))
        e.name=input('Enter employee name : ')
        e.year=int(input('Enter year of joining : '))
    def display(e):
        print(f'Employee code : {e.code}')
        print(f'Employee name : {e.name}')
        print(f'Employee year of joining : {e.year}')
n=int(input('Enter number of Employees : '))
elist=[]
for i in range(0,n):
    print(f'Enter employee {i+1} details:')
    e=Employee()
    e.read()
    elist.append(e)
cyear=int(input('Enter current year : '))
for i in range(0,n):
    e=elist[i]
    if(cyear-e.year>=3):
        e.display()