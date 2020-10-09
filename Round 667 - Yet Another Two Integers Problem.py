# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:36:49 2020

@author: amray
"""
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    moves = 0
    difference = abs(a-b)
    moves = difference // 10
    difference = difference - (moves*10)
    if difference != 0:
        moves+=1
    print(moves)
    
        
    