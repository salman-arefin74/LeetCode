class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for n in prices:
          if n < min_so_far:
            min_so_far = n
          max_profit = max(max_profit, n-min_so_far)
            
        return max_profit