# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:36:17 2020

@author: amray
"""

#%%
counter = int(input())

for i in range(counter):
    n = int(input())
    array = [int(i) for i in str(n)]
    size = len(array)
    index = 0
    result = []
    for i in range(size-1, -1, -1):
        if array[index] != 0:
            result.append(array[index]*(10**i))
        index+=1
    print(len(result))
    for i in result:
        print(i, end = ' ')