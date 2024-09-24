class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        a = [[] for _ in range(n)]
        for i in range(n):
            if i == headID:
                continue
            a[manager[i]].append(i)
        b = []
        def dfs(n,m):
            if len(n) == 0:
                b.append(m)
                return
            for i in n:
                dfs(a[i], informTime[i] + m)
        dfs(a[headID], informTime[headID])
        return max(b)
