class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        d = dict()
        
        for right, c in enumerate(s):
            if c in d:
                left = max(d[c] + 1, left)
            d[c] = right
            res = max(res, right - left + 1)
        return res
            
