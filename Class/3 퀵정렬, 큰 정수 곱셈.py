# 빠른 정렬
def quickSort(s, low, high):
    if high > low:
        partition(s, low, high)
        pivotpoint = partition(s, low, high)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high)

def partition(s, low, high):
    pivotitem = s[low]
    j = low
    for i in range(low+1, high+1):
        if s[i] < pivotitem:
            j=j+1
            s[i], s[j] = s[j], s[i]
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

s = [3, 5, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)

# 큰 정수 곱셈

import math

def prod2(a, b):
    n = max(len(str(a)), len(str(b)))
    if a == 0 or b == 0: return 0
    elif n <= 4: return a*b
    else:
        m = math.floor(n/2)
        x = a//(10**m)
        y = a%(10**m)
        w = b//(10**m)
        z = b%(10**m)
        r = prod2(x+y, w+z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p*(10**(2*m)) + (r-p-q)*(10**m) + q

a = 1234567812345678
b = 2345678923456789

print(prod2(a, b))
print(a*b)
