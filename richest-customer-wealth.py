class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for row in accounts:
          if richest < sum(row):
            richest = sum(row)
            
        return richest
        