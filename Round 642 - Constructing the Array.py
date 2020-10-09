# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:24:52 2020

@author: amray
"""
#%%
def recurse(start, end, log):
    if start > end:
        return
    else:
        mid = (start+end)//2
        log.append((start, mid, end))
        recurse(mid+1, end, log)
        recurse(start, mid-1, log)
  
    
for _ in range(int(input())):
    size = int(input())
    memo = []
    recurse(0, size-1, memo)
    memo = sorted(memo, key = lambda x:(x[2]-x[0], -x[0]), reverse = True)
    ans = [0]*size
    for i in range(len(memo)):
        ans[memo[i][1]] = i+1
    
    print(*ans)
