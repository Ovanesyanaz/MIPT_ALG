def route_exists(g: list[list[int]], v: int, u: int) -> bool:
    col = [0] * len(g)

    def dfs_for_x(y: int, x) -> bool:
        col[y] = 1
        if x in g[y]:
            return True
        for curr in g[y]:
            if (col[curr] == 0) and dfs_for_x(curr, x):
                return True
        return False

    return dfs_for_x(v, u) and dfs_for_x(u, v)
