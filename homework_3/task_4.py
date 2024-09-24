class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        unique_colors = set(colors)

        a = [[] for i in range(n)]
        for i in edges:
            a[i[0]].append(i[1])

        def topo_sort(graph: list[list[int]]) -> list[int]:
            n = len(graph)
            visited = [0] * n
            order = []

            def dfs(vert: int):
                visited[vert] = 1
                for adj in graph[vert]:
                    if visited[adj] == 0:
                        dfs(adj)
                    if visited[adj] == 1:
                        return -1
                
                visited[vert] = 2
                order.append(vert)

            b = []
            prev = 0
            for vert in range(n):
                if not visited[vert]:
                    if dfs(vert) == -1:
                        return -1
                    
                    cur = sum(visited) // 2
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
        
        topo = topo_sort(a)
        if topo == -1:
            return -1
        
        mx = -1
        cache = []

        def dfs(vert, char):
            if cache[vert] != -1:
                return cache[vert]
            count = 0
            for adj in a[vert]:
                count = max(count, dfs(adj, char))
            if char == colors[vert]:
                count += 1
            cache[vert] = count
            return count
        for component in topo:
            head = component[0]
            for char in set(colors):
                cache = [-1] * n
                mx = max(mx, dfs(head, char))

        return mx