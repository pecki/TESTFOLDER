# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:14:43 2017

@author: pecki
"""
a = ['it']
b = ['was']
e = ['just']
c = ['awful']
d = a + b + e + c
print(d)

s = ''
for x in d:
    s += x
    
print(s)

# Find the sum of the integers from 1-249:
sum_100 = 0
for i in list(range(1, 250)):
    sum_100 += i
    
print(sum_100)

string = "RPI is my college, but my hometown is Lancaster."
cnt = string.count('i')
print(cnt)

newcnt = s.count('t')
print(newcnt)

print("Hi, How Are You?")

u = "We should do a group dinner on Wednesday night gggg"
ucnt = u.count('g')
print(ucnt)