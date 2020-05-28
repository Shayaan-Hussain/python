# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:54:39 2020

@author: Shayaan
"""

from random import randint
def flip():
    if(randint(0,2)==1):
        return True
    else:
        return False
while True:
    try:
        n=int(input('Enter number of flips : '))
    except:
        print('Entered data is not integer')
    else:
        break
heads=0
tails=0
result=[]
for i in range(0,n):
    if(flip()):
        heads+=1
        result.append('H')
    else:
        tails+=1
        result.append('T')
print('Result : ',end='')
for i in result:
    print(f' {i}',end='')
print(f'\n1Number of heads : {heads}')
print(f'Number of tails : {tails}')