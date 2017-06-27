# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:14:43 2017

@author: pecki
"""
a = ['it']
b = ['was']
e = ['just']
c = ['terrible']
d = a + b + e + c
print(d)


s = ''
for x in d:
    s += x
    
print(s)

# Find the sum of the integers from 1-100:
    
sum100 = 0
for i in list(range(1, 101)):
    sum100 += i
    
print(sum100)

string = "RPI is my university, but my hometown is Buffalo."
cnt = string.count('i')
print(cnt)

newcnt = s.count('t')
print(newcnt)

print("SUP")

u = "We should do a group dinner on Wednesday night gggg"
ucnt = u.count('g')
print(ucnt)