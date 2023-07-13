# Find Eventual Safe States

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe
            safe[i] = False
            for padosi in safe[i]:
                if not dfs(padosi):
                    return safe[i]
            safe[i] = True
            return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
