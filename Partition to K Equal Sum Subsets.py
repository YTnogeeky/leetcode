class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visit = [0 for i in range(len(nums))]
        target= sum(nums) // k
        def DFS(k, fromindex, cursum):
            if k == 1 and cursum == target:
                return True
            if cursum == target:
                return DFS(k-1, 0, 0)
            else:
                for i in range(fromindex, len(nums)):
                    if nums[i] + cursum <= target and not visit[i]:
                        visit[i] = 1
                        if DFS(k, i + 1, cursum + nums[i]):
                            return True
                        visit[i] = 0
                return False
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        return DFS(k, 0, 0)
