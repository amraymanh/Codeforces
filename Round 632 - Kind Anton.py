# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:07:30 2020

@author: amray
"""

#%%
counter = int(input())

for x in range(counter): 
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    one, neg = False, False
    if a==b:
        print('YES')
        continue   
    if(a[0] != b[0]):
        print('NO')
        continue
    if a[0] == 1:
        one = True
    if a[0] == -1:
        neg = True
        
    found = True
    for i in range(1, n):
        if(a[i]<b[i] and not one):
            found = False
            print('NO')
            break
        elif(a[i] > b[i] and not neg):
            found = False
            print('NO')
            break
        if a[i] == 1:
            one = True
        if a[i] == -1:
            neg = True
    if found:
        print('YES')
        
    
            