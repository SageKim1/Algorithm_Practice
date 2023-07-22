class Solution:
    # Time complexity: O(n) | the time grows linearly
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        # O(n) | iterate through the entire array of prices once
        for price in prices:
            # O(1) | constant time operation
            min_price = min(min_price, price)
            # O(1) | constant time operation
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
