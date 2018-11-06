class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxcur, maxsofar = 0, 0
        
        for i in xrange(1, len(prices)):
            maxcur += prices[i] - prices[i-1]
            print maxcur
            maxcur = max(0, maxcur)
            maxsofar = max(maxcur, maxsofar)
            
            
        return maxsofar
