class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        nums = xrange(1,10)
        self.dfs(nums, k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)
