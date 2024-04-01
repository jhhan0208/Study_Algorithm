def seqsearch(s, x): 
    loc = 0
    while loc < len(s) and s[loc] != x:
        loc = loc+1
    if loc >= len(s): loc = -1
    return loc

s=[3, 5, 2, 1, 7, 9]
loc = seqsearch(s, 4)
print(loc)

#__________________________________________

s=[3,2,5,7,1,9,4,6,8]
n = len(s)
for i in range(0, n-1):
    for j in range(i+1, n):
        if s[j] < s[i]:
            s[j], s[i] = s[i], s[j]

print(s)
