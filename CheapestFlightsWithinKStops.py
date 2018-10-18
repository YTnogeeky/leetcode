class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        remain, ret, stop = [], sys.maxint, 0
        weights = [sys.maxint for i in range(n)]
        graph = [{} for i in range(n)]
        for s,d,w in flights:
            graph[s][d]=w

        heapq.heappush(remain, (0, src))
        weights[src] = 0
        while remain and stop <= K:
            tmp, remain = remain, []
            while tmp:
                weight, node = heapq.heappop(tmp)
                for tonode, toweight in graph[node].items():
                    if weights[tonode] > weight + toweight:
                        weights[tonode] = weight + toweight
                        heapq.heappush(remain, (weights[tonode], tonode))    
                    # this two lines are important
                    if tonode == dst and weights[tonode]<ret:
                        ret = weights[tonode]
            stop+=1
        return ret if ret < sys.maxint else -1
