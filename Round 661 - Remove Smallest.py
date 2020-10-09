# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 00:04:41 2020

@author: amray
"""

t = int(input())
for _ in range(t):
    size = int(input())
    a = map(int, input().split())
    if size == 1:
        print('YES')
        continue
    sortedd = sorted(a)
    check = True
    for i in range(1, size):
        if (sortedd[i] - sortedd[i-1]) > 1:
            check = False
            break
    print('YES' if check else 'NO')