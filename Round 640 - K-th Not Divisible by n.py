# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:03:09 2020

@author: amray
"""
#%%
import math
counter = int(input())
for i in range(counter):
    n, k = map(int, input().split())
    growthfactor = n - 1
    level = math.ceil(k / growthfactor)
    start = n*(level-1)+1
    currentk = growthfactor*(level-1)+1
    result = start + (k-currentk)
    print(result)
