class Solution(object):
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            print "cur", curSum
            maxSum = max(maxSum, curSum)
            print maxSum

        return maxSum
