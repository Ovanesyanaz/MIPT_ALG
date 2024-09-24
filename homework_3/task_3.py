def min_added_edges(comp_graph):
    n = len(comp_graph)
    source = 0  # вершины источники
    drain = 0  # вершины стоки
    isolated = 0  # вершины изолированные
    edge_starts = []
    edge_ends = []
    for i in range(n):
        for adj in comp_graph[i]:
            edge_starts.append(i)
            edge_ends.append(adj)
    for i in range(n):
        if i in edge_starts:
            source += 1
        elif i in edge_ends:
            drain += 1
        else:
            isolated += 1
    return max(isolated+source, isolated+drain)