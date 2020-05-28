class Fibonacci():
    def __init__(a,n):
        a.n=n
    def calc(a):
        a1=0
        a2=0
        a3=1
        i=0
        for a in range(i,a.n):
            a1=a1+a2
            a2=a3
            a3=a1
            print(a1)
i=int(input('Enter number of terms : '))
f=Fibonacci(i)
f.calc()