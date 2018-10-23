class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        res = 0
        for i in nums:
            s.add(i)
            
        for j in nums:
            if j in s:
                s.remove(j)
                
                down = j - 1
                up = j + 1
                while up in s:
                    s.remove(up)
                    up = up + 1
                while down in s:
                    s.remove(down)
                    down = down - 1
                
            res = max(res, up - down -1)
            
                
        return res
