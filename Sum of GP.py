class GPSum():
    def __init__(gp,first,n,cr):
        gp.first=first
        gp.n=n
        gp.cr=cr
    def sum(gp):
        print(f'Sum of GP = {gp.first*(1-gp.cr**gp.n)/(1-gp.cr)}')
f=int(input('Enter the first term of GP : '))
total=int(input('Enter the total number of terms : '))
ratio=int(input('Enter the common ratio : '))
gp=GPSum(f,total,ratio)
gp.sum()