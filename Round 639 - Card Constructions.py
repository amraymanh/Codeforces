# -*- coding: utf-8 -*-
#%%
import math

counter = int(input())
for i in range(counter):
    num = int(input())
    count = 0
    while num >= 2:  
        temph = int(math.sqrt(0.5*num))
        summ = int((3/2)*temph**2 + (temph/2))
        nexth = temph+1
        nextsum = int((3/2)*nexth**2 + (nexth/2))
        while nextsum <= num:
            temph = nexth
            summ = nextsum
            nexth+=1
            nextsum = int((3/2)*nexth**2 + (nexth/2))
        if temph > 0:
            count+=1
        num = num - summ
    print(count)