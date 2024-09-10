from enum import Enum
class Color(Enum):
    WHITE = 0,
    BLACK = 1,

def topological_sort(g: list[list[int]]) -> bool:
    c = [Color.WHITE]*len(g)
    order = []
    
    def dfs(v : int):
        c[v] = Color.BLACK
        for u in g[v]:
            if c[u] == Color.WHITE:
                dfs(u)
        order.append(v)
    for i in range(len(g)):
        if c[i] == Color.WHITE:
            dfs(i)
    order.reverse()
    return order

d = ["Пиджак",
     "Часы",
     "Брюки",
     "Рубашка",
     "Трусы",
     "Носки",
     "Туфли",
     "Галстук",
     "Ремень"]

adj = [[],
       [],
       [6,8],
       [8,7],
       [2,6],
       [6],
       [],
       [0],
       [0]
       ]

answ = topological_sort(adj)
for i in answ:
    print(d[i])