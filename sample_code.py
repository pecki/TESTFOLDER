# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:14:43 2017

@author: pecki
"""
a = ['it']
b = ['was']
c = ['bad']
d = a + b + c
print(d)


s = ''
for x in d:
    s += x
    
print(s)

# Find the sum of the integers from 1-100:
    
sum100 = 0
for i in list(range(1, 101)):
    print(i)
    sum100 += i
    
print(sum100)