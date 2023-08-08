class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        bought_price = float("inf")
        total_profit = 0

        for i in range(len(prices)):
            if prices[i] > bought_price:
                total_profit += prices[i] - bought_price
                bought_price = prices[i]
            elif prices[i] < bought_price:
                bought_price = prices[i]
        
        return total_profit
