class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        g = []
        for i in isConnected:
            h = []
            for j in range(len(i)):
                if i[j]:
                    h.append(j)
            g.append(h)
        def topological_sort(g: list[list[int]]) -> bool:
            c = [0]*len(g)
            amount_elem = 0
            def dfs(v : int):
                c[v] = 1
                for u in g[v]:
                    if c[u] == 0:
                        dfs(u)
            for i in range(len(g)):
                if c[i] == 0:
                    dfs(i)
                    amount_elem += 1
            return amount_elem
        answ = topological_sort(g)
        return answ
