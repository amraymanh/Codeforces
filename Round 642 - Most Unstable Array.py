import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        continue
    elif n == 2:
        print(m)
        continue
    else:
        print(m*2)