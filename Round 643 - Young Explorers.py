def solve(data,size):
    counter = 0
    i = 0
    while i < size:
        new_index = i + data[i] -1 
        if new_index < size: 
            if data[new_index] == data[i]:
                i = new_index+1
                counter+=1
            else:
                new_index+=1
                while new_index<size and (new_index-i+1) < data[new_index] :
                    new_index+=1
                if new_index == size:
                    return counter
                else:
                    counter+=1
                    i = new_index+1
        else:
            return counter
    return counter
 
for _ in range(int(input())):
    size = int(input())
    if size == 1:
        data = int(input())
        print(1 if data == 1 else 0)
    else:
        data = list(map(int, input().split()))
        data = sorted(data)
        print(solve(data, size))