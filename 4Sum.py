class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                l, r = j + 1, length - 1
                while l < r:
                    if nums[l] + nums[r] == sum:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                        l += 1
                    elif nums[l] + nums[r] > sum:
                        r -= 1
                    else:
                        l += 1
        return res
