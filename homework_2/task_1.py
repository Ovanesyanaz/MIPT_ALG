def topological_sort(graph: list[list[int]]):
    visit = [False] * len(graph)
    order = []
    arr = list(range(len(graph)))
    while len(arr) != 0:
        if visit[arr[0]] == 1:
            arr.pop(0)
            continue
        flag = False
        for i in graph[arr[0]]:
            if visit[i] == 0:
                flag = True
                break
        if flag:
            arr.append(arr.pop(0))
        else:
            order.append(arr[0])
            visit[arr[0]] = 1
    return order[::-1]

vertices = [
    "Пиджак", 
    "Часы",
    "Брюки",
    "Рубашка",
    "Трусы",
    "Носки",
    "Туфли",
    "Галстук",
    "Ремень"
]

adj_list = [[], [], [6, 8], [8, 7], [2, 6], [6], [], [0], [0]]

print(*map(lambda x: vertices[x], topological_sort(adj_list)))