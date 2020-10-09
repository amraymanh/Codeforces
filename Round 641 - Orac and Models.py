def solve(size, data):
    log = [1]*(size)  
    for i in range(((size-1)//2), -1, -1):
        for j in range(2* i +1 , size, i+1):
            if data[i] < data[j]:
                log[i] = max(log[i], log[j]+1)
    return max(log)
    
counter = int(input())
for _ in range(counter):
    size = int(input())
    data = [int(i) for i in input().split()]
    print(solve(size, data))