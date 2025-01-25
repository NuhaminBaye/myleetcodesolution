class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize min_price to a very high value
        max_profit = 0  # Initialize max_profit to zero
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if a lower price is found
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if a higher profit is found
        
        return max_profit