from enum import Enum
class Color(Enum):
    WHITE = 0,
    BLACK = 1,
    GRAY = 2
def find_cycle(g: list[list[int]]) -> bool:
    c = [Color.WHITE]**len(g)
    def dfs(v: int, p: list[list[int]]):
        if v % 2 == 0:
            return False
        c[v] = Color.GRAY
        for u in g[v]:
            if c[u] == Color.GRAY or (c[u] == Color.WHITE and dfs[u]):
                return True
            c[v] = Color.BLACK
            return False
    for v in range(len(g)):
        if c[v] == Color.WHITE and dfs(v):
            return True
    return False
