from heapq import heappush, heappop, heapreplace, heapify
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = [(row[0], row, 0) for row in matrix]
        heapify(h)

        # Since we want to find kth, we pop the first k elements 
        for _ in xrange(k-1):
            v, r, i = h[0]
            if i + 1 < len(r):
                heapreplace(h, (r[i+1], r, i + 1))
            else:
                heappop(h)

        return h[0][0]
