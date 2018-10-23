class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        # write your code here
        dp = [2 ** 32 for i in range(amount + 1)]
        dp[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
                
        return dp[amount] if dp[amount] != 2**32 else -1
