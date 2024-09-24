from typing import List


def transpose_graph(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    new_adj = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            new_adj[j].append(i)
    return new_adj


def topo_sort(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [0] * n
    order = []

    def dfs(vert: int):
        visited[vert] = 1
        for adj in graph[vert]:
            if not visited[adj]:
                dfs(adj)
        order.append(vert)
    b = []
    prev = 0
    for vert in range(n):
        if not visited[vert]:
            dfs(vert)
            cur = sum(visited)
            b.append(cur - prev)
            prev = cur
    order = order[::-1]
    c = []
    s = 0
    for i in b:
        d = []
        for j in range(i):
            d.append(order[j + s])
        c.append(d)
        s += i
    return c


def strong_components(graph: List[List[int]]) -> List[int]:
    t = transpose_graph(graph)
    topo_sorted = topo_sort(graph)
    n = len(graph)

    component_index = [-1] * n
    current_comp = 0

    def dfs(vert: int):
        component_index[vert] = current_comp
        for adj in t[vert]:
            if component_index[adj] == -1:
                dfs(adj)

    for vert in topo_sorted:
        if component_index[vert] == -1:
            dfs(vert)
            current_comp += 1

    return component_index


def component_graph(graph, comp_ind):
    comp_n = max(comp_ind)
    comp_adj = [[] for _ in range(comp_n)]

    for vert in range(len(graph)):
        cur_comp = comp_ind[vert]
        for adj in graph[vert]:
            adj_comp = comp_ind[adj]
            if adj_comp != cur_comp and adj_comp not in comp_adj[cur_comp]:
                comp_adj[cur_comp].append(adj_comp)

    return comp_adj

adj_list = [
    [1,2],
    [],
    [3],
    [4],
    []
]

print(topo_sort(adj_list))
