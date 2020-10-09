# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:12:37 2020

@author: amray
"""
#%%
counter = int(input())
for c in range(counter):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print(n+(2*k))
        continue
    else:
        prime = True
        for j in range(3, int(n / 2) + 1, 2):
            if n % j == 0:
                n = n + j
                prime = False
                break
        if prime:
            print((2*n)+ (2 * (k-1)))
        else:
            print(n+ (2 * (k-1)))
        