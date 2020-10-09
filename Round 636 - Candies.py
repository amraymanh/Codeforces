counter = int(input())
for i in range(counter):
    num = int(input())
    
    temp = 2
    while(temp<= num):
        temp = temp * 2
        x = num/(temp-1)
        if x.is_integer():
            print(int(x))
            break