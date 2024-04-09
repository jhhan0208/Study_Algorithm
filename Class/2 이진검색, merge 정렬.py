def bs(data, item, low, high):

    if low > high: return 0
    else:
        mid = (low + high)//2
        if item == data[mid]: return mid
        elif item < data[mid]: return bs(data, item, low, mid-1)
        else: return bs(data, item, mid+1, high)

data = [1,3,5,6,7,9,10,14,17,19]
n = 10
location = bs(data, 17, 0, n-1)
print(location)

#_________________________________________________

def mergeSort(n, s):
    h = n//2
    m = n-h

    if n>1:
        u = s[:h]
        v = s[h:]
        mergeSort(h, u)
        mergeSort(m, v)
        merge(h, m, u, v, s)
    
def merge(h, m, u, v, s):
    i = 0
    j = 0
    k = 0

    while i < h and j < m:
        if u[i] < v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1

    while i < h:
        s[k] = u[i]
        i += 1
        k += 1

    while j < m:
        s[k] = v[j]
        j += 1
        k += 1

s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSort(8, s)
print(s)
