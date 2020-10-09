import math
 
def solve(data, size):
    result = [0]*size
    result[-1] = data[-1]
    for i in range(size-2, -1, -1):
        result[i] = math.gcd(result[i+1] , data[i])
    for i in range(size-1):
        result[i] = data[i] * result[i+1] // math.gcd(data[i], result[i+1])
    result.pop()
    ans = result[0]
    for i in range(1, len(result)):
        ans = math.gcd(ans, result[i])
    return ans

size = int(input())
data = list(map(int, input().split()))
 
print(solve(data, size))