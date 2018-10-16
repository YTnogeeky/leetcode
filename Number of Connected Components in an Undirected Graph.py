class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
         
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x = find(e[0])
            y = find(e[1])
            if x != y:
                n -= 1 
                parent[x] = y
        return n
