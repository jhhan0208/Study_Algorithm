# Dijkstra의 알고리즘

inf=1000
w=[
[0,3,2,8,inf,inf],
[inf,0,1,inf,5,inf],
[inf,inf,0,5,3,inf], 
[inf,inf,inf,0,3,2], 
[inf,inf,inf,inf,0,1],
[inf,inf,inf,inf,inf,0]
]
n=6

f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]

for i in range(1,n):
    length[i]=w[0][i]

for _ in range(n-1):
    minn = inf
    for i in range(1, n):
        if 0 <= length[i] < minn:
            minn = length[i]
            save_length[i] = minn
            vnear = i
    e = (touch[vnear], vnear)
    f.add(e)
    for i in range(1, n):
        if (length[vnear]+ w[vnear][i] < length[i]):
            length[i] = length[vnear] + w[vnear][i]
            touch[i] = vnear
    length[vnear]=-1

# 추가 부분

lf = list(f)
lf.sort(key=lambda p: (p[1]))

for i in range(n-1):
    s = lf[i][0]
    e = lf[i][1]
    L = []
    L.append(e)
    L.append(s)

    j = 0
    while s != 0:
        if lf[j][1] == s:
            L.append(lf[j][0])
            s = lf[j][0]
        j = j+1
        if j >= n-1: j = -1
        
    print(f'<노드 {chr(i+98)}>')
    print('최단경로: ', end = '')
    for k in range(len(L)-1,-1,-1):
        print(f'{chr(L[k]+97)}', end = '-')
    print()
    print(f'최단거리: {save_length[i+1]}', end = ' ')
    print()
    print()

mi = save_length.index(min(save_length[1:]))
ma = save_length.index(max(save_length))
print(f'가장 짧은 길이 및 노드: {save_length[mi]}, {chr(mi+97)}')
print(f'가장   긴 길이 및 노드: {save_length[ma]}, {chr(ma+97)}')
