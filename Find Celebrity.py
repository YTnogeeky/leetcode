class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1,n):
            if knows(ans, i):
                ans = i
        
        for i in range(0, n):
            if i!=ans and knows(ans, i):
                return -1
            if i!=ans and not knows(i, ans):
                return -1
        return ans
