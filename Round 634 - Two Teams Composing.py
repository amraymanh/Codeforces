# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:39:19 2020

@author: amray
"""

#%%



counter = int(input())

for i in range(counter):
    students = int(input())
    skills = [int(x) for x in input().split()]
    if(students == 1):
        print(0)    
    else:   
        memo = {}
        
        maxcount = 1    
        for i in skills:
            if(i in memo):
                memo[i]+=1
                if(memo[i]>maxcount):
                    maxcount = memo[i]
            else:
                memo[i] = 1
                
        notmax = len(memo)-1
        if(maxcount - notmax >= 2):
            print(notmax+1)
        elif(maxcount >= notmax):
            print(notmax)
        elif(maxcount < notmax):
            print(maxcount)
        elif(maxcount == 1):
            print(1)

