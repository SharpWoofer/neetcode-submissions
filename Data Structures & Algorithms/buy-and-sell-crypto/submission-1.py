class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        L, profit = 0,0
        for R in range(1, len(prices)):
            if prices[R] < prices[L]: L = R
            curr_profit = prices[R] - prices[L]
            profit = max(curr_profit, profit)
        return profit