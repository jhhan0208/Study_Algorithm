# Prim의 알고리즘

import utility

inf = 1000
w=[[0, 1, 3,inf, inf],
    [1, 0, 3,6, inf],
    [3, 3, 0,4, 2],
    [inf,6, 4,0, 5],
    [inf,inf,2,5, 0]]

F=set()
utility.printMatrix(w)
n=len(w)
nearest=n*[0]
distance=n*[0]
for i in range(1,n):
    nearest[i]=0
    distance[i]=w[0][i]

for _ in range(n-1):
    min = inf
    for i in range(1, n):
        if 0 <= distance[i] < min:
            min = distance[i]
            vnear = i

    e = (vnear, nearest[vnear])
    F.add(e)
    distance[vnear] = -1

    for i in range(1, n):
        if w[i][vnear] < distance[i]:
            distance[i] = w[i][vnear]
            nearest[i] = vnear

print()
print(F)
print()

# __________________________________________________________
# Kruskal의 알고리즘

parent = dict()
rank = dict()

def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: rank[r2] += rank[r1]

def kruskal(graph):
    E = sorted(list(graph.get('edges')))
    F = set()
    n = len(graph.get('vertices'))
    for i in range(n): make_singleton_set(i)
    c = 0
    while len(F) < n-1:
        e = E[c]
        c = c+1
        i = graph.get('vertices').index(e[1])
        j = graph.get('vertices').index(e[2])
        p = find(i)
        q = find(j)
        if p != q:
            union(p, q)
            F.add(e)
    
    return F

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (3, 'B', 'C'),
            (6, 'B', 'D'),
            (4, 'C', 'D'),
            (2, 'C', 'E'),
            (5, 'D', 'E'),
            ])
        }
mst=kruskal(graph)
print(mst)

print()
