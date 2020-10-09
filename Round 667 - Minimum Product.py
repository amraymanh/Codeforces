# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:41:02 2020

@author: amray
"""
t = int(input())
for _ in range(t):
    
    a, b, x, y, n = map(int, input().split())

    diffa = min(a-x, n)
    diffb = min(b-y, n)
    
    
    if a-diffa <= b-diffb:
        a-=diffa
        n-=diffa
        b-=min(b-y, n)
    elif a-diffa > b-diffb:
        b-=diffb
        n-=diffb
        a-=min(a-x, n)
    print(a*b)
        