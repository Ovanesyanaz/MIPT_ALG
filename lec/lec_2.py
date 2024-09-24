def bfs(g:list[list[int]], v:int):
    print(v)
    a = []
    for i in g[v]:
        a.append(i)
    while len(a) > 0:
        print(a[0])
        for i in g[a[0]]:
            a.append(i)
        a.pop(0)
adj = [
    [1,2,3],
    [4,5],
    [6],
    [7],
    [],
    [],
    [],
    []
]

bfs(adj, 0)