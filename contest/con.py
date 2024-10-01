def to_adj(n,m):
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    a = [[] for i in range(n)]
    for i in edges:
        a[i[0]].append(i[1])
        a[i[1]].append(i[0])
    for i in range(len(a)):
        a[i].sort()
    return a
n,m = map(int, input().split())

color = [0] * n
flag = True

def dfs(n, adj, k):
    global flag
    if color[n] == 0:
        color[n] = k
        for u in adj[n]:
            dfs(u, adj, -k)
    elif color[n] != k:
        flag = False
dfs(0, to_adj(n,m), 1)
if flag:
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")