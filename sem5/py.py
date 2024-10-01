def is_eiler_graph_undir(graph: list[list[int]]) -> bool:
    odd_vertex = 0
    for a in graph:
        if (len(a) % 2):
            odd_vertex += 1
    if odd_vertex > 2:
        return False
    return True

def topo_sort(graph: list[list[int]]) -> bool:
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
            if len(order) != 1:
                b.append(order[::-1])
            order.clear()
    return (len(b) == 1)
