# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:50:28 2020

@author: amray
"""

t = int(input())
for _ in range(t):
    size = int(input())
    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    minCandy = min(candies)
    minOranges = min(oranges)

    moves = 0
    for i in range(size):
        diffCandy = candies[i] - minCandy
        diffOranges = oranges[i] - minOranges
        moves+=max(diffCandy, diffOranges)
    print(moves)