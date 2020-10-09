# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:11:12 2020

@author: amray
"""
#%%

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if b >= (2*a):
        print(n*a)
    else:
        if n % 2 == 0:
            print((n//2)*b)
        else:
            print(((n//2)*b)+a)