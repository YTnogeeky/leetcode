class Solution(object):
    
    def validTree(self, n, edges):
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x = find(e[0])
            y = find(e[1])
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1
