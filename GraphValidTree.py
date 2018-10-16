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

import collections
class Solution:
  def validTree(self, n, edges):
    if len(edges) != n - 1:
      return False

    neighbors = collections.defaultdict(list)
    for k, v in edges:
      neighbors[k].append(v)
      neighbors[v].append(k)

    visited = []
    queue = [0]
    while queue:
      cur = queue.pop()
      visited.append(cur)
      queue += [node for node in neighbors[cur] if node not in visited]
  
    return len(visited) == n
    
    
