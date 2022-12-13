class Solution:
    # TC: O(n)
    # MC: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        profit = 0
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif prices[i] - minPrice > profit:
                profit = prices[i] - minPrice
        return profit
