# 그래프의 깊이우선검색/너비우선검색 

import utility
import queue

e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)]

for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
            if j in e[i]:
                a[i][j]=1
                a[j][i]=1

utility.printMatrix(a)

visited_dfs = n*[0] # dfs 방문 확인용
visited_bfs= n*[0] # bfs 방문 확인용

# 깊이 우선검색 구현
def DFS(a,v):
    if visited_dfs[v] == 0: 
        visited_dfs[v] = 1
        print(v)
        for i in range(len(a)):
            if a[v][i] == 1: DFS(a, i)

print('DFS:')
DFS(a,0)

# 너비 우선검색 구현
def BFS(a,v):
    q=queue.Queue()
    q.put(v)
    while(not q.empty()):
        x = q.get()
        if visited_bfs[x] == 0: 
            visited_bfs[x] = 1
            print(x)
        for i in range(len(a)):
            if a[x][i] == 1 and visited_bfs[i] == 0: q.put(i)

print('BFS:')
BFS(a,0)

# _______________________________________________________________
# 5-Queens problem

def promising(i,col):
    k = 0
    switch = True
    while k<i and switch:
        if col[i]==col[k] or abs(col[i]-col[k])==i-k:
            switch = False
        k = k+1
    return switch

def queens(n,i,col):
    if promising(i,col):
        if i==n-1:
            print(col)
        else:
            for j in range(0, n):
                col[i+1]=j
                queens(n, i+1, col)
                           
n = 5
col = n*[0]
queens(n, -1, col)
