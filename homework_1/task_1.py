def from_adjacency_list_to_edge_list(g: list[int]) -> list[tuple[int, int]]:
    n = len(g)
    el = []
    for i in range(n):
        for v in g[i]:
            el.append((i, v))
    return el


def from_adjacency_list_to_adjacency_matrix(g: list[list[int]]) -> list[list[int]]:
    n = len(g)
    am = [[0]*n for _ in range(n)]
    for i in range(n):
        for v in g[i]:
            am[i][v] = 1
    return am


def from_adjacency_matrix_to_adjacency_list(am: list[list[int]]) -> list[list[int]]:
    n = len(am)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if am[i][j] == 1:
                g[i].append(j)
    return g


def from_adjacency_matrix_to_edge_list(am: list[list[int]]) -> list[tuple[int, int]]:
    n = len(am)
    el = []
    for i in range(n):
        for j in range(n):
            if am[i][j] == 1:
                el.append((i, j))    
    return el


def from_edge_list_to_adjacency_list(el: list[tuple[int, int]]) -> list[list[int]]:
    n = 0
    for edge in el:
        n = max(max(edge), n)
    g = [[] for _ in range(n)]
    for edge in el:
        g[edge[0]].append(edge[1])
    return g


def from_edge_list_to_adjacency_matrix(el: list[tuple[int, int]]) -> list[list[int]]:
    n = 0
    for edge in el:
        n = max(max(edge), n)
    am = [[0]*n for _ in range(n)]
    for edge in el:
        am[edge[0]][edge[1]] = 1
    return am
