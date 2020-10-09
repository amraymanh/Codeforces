counter = int(input())
 
for i in range(counter):
    num = int(input())
    if(num%2 == 0):
        print((num//2)-1)
    else:
        print(num//2)