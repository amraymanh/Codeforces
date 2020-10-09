# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:17:27 2020

@author: amray
"""
#%%

counter = int(input())

for z in range(counter):
    n, a, b = [int(x) for x in input().split()]    
    distinct = 0    
    word = ''  
    index = 0
    while(len(word) != n):
        sub = word[index:]
        distinct = len(set(sub))
        lett = ord('a')
        while(distinct < b):
            while (chr(lett) in sub):
                lett+=1
            word = word + chr(lett)
            sub = sub + chr(lett)
            distinct+=1
        keys = list(set(sub))
        size = len(keys)
        temp = 0
        while(len(sub) < a):
            sub = sub + keys[temp]
            word = word + keys[temp]
            temp = (temp + 1)%size
        index+=1
    print(word)      
