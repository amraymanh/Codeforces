
#%%
def draw(arr, size, i, j, value):
    arr[i][j] = value
    arr[i][size-1-j] = value
    arr[size-1-i][j] = value
    arr[size-1-i][size-1-j] = value

def drawRow(arr, size, index, value):
    arr[index][size//2] = value
    arr[size-1-index][size//2] = value

def drawCol(arr, size, index, value):
    arr[size//2][index] = value
    arr[size//2][size-1-index] = value
    
def printt(arr, size):
    for i in range(size):
        print(*arr[i])
        
size = int(input())
items = list(map(int, input().split()))
log = {}
quads = []
twos = []
one = -1
x = False
for i in items:
    if i in log:
        log[i]+=1
        if log[i] % 4 == 0:
            quads.append(i)
    else:
        log[i]=1
for key,value in log.items():
    if value % 4 == 1:
        one = key
    if value % 4 == 3:
        if one != -1:
            x = True
        else:
            twos.append(key)
            one = key
    elif value % 4 == 2: 
        twos.append(key)
if size % 2 == 0:
    if (size/2)**2 == len(quads):
        print('YES')     
        drawing = [[0]*size for i in range(size)]
        for i in range(size//2):
            for j in range(size//2):
                value = quads.pop()
                draw(drawing, size, i, j, value)
        printt(drawing,size)
    else:
        print('NO')
else:
    if len(quads) < ((size//2)**2) or one == -1 or x:   
        print('NO')
    else:
        temp4 = len(quads) - ((size//2)**2)
        temp2 = len(twos) + (temp4*2)
        if temp2 == (size-1):
            print('YES')
            drawing = [[0]*size for i in range(size)]       
            for i in range(size//2):
                for j in range(size//2):
                    value = quads.pop()
                    draw(drawing, size, i, j, value)
            while(len(quads)>0):
                value = quads.pop()
                twos.append(value)
                twos.append(value)
            for i in range(size//2):
                value = twos.pop()
                drawRow(drawing, size, i, value)
                value = twos.pop()
                drawCol(drawing, size, i, value)
            drawing[size//2][size//2] = one
            printt(drawing, size)
        else:
            print('NO')   
        