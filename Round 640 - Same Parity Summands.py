# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:05:22 2020

@author: amray
"""
#%%
counter = int(input())
for i in range(counter):
    n, k = map(int, input().split())
    if k > n:
        print('NO')
    elif n%2 == 1 and k%2 == 0:
        print('NO')
    elif n%2 == 1 and k%2 == 1:
        summ = 0
        print('YES')
        for i in range(k-1):
            summ+=1
            print(1, end = ' ')
        print(n-summ)  
    elif n%2 == 0 and k%2 == 1:
        if n/k < 2:
            print('NO')
        else:
            summ = 0
            print('YES')
            for i in range(k-1):
                summ+=2
                print(2, end = ' ' )
            print(n - summ)
    elif n % 2 == 0 and k%2 == 0:
        parity = n//k
        if parity < 1:
            print('NO')
        else:
            print('YES')
            summ = 0
            for i in range(k-1):
                summ+=parity
                print(parity, end = ' ')
            print(n-summ)