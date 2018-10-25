class Solution(object):
    def wordBreak(self, s, words):
        d = [False] * (len(s) + 1)
        d[0] = True
        
        for i in range(0, len(s)):
            for j in range(i, -1, -1):
                if s[j:i+1] in words and d[j] == True:
                    d[i+1] = True
        return d[-1]
