def topo_sort(graph: list[list[int]]) -> list[int]:
    n = len(graph)
    visited = [0] * n
    order = []

    def dfs(vert: int):
        visited[vert] = 1
        for adj in graph[vert]:
            if visited[adj] == 0:
                dfs(adj)
        order.append(vert)

    b = []
    for vert in range(n):
        if not visited[vert]:
            dfs(vert)
            b.append(order[::-1])
            order.clear()
    return b

def answ(g, b):
    for i in b:
        g[i[0]].remove(i[1])
        g[i[1]].remove(i[0])
    return topo_sort(g)

adj_list = [
    [1,3],
    [0,2],
    [1,3,5],
    [0,2],
    [5,7],
    [4,6,2],
    [5,7],
    [4,6]
]
print(answ(adj_list, [[2,5]]))