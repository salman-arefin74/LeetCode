class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        i = 0
        while (total - i*cost1) >= 0:
          temp = total - i*cost1
          ways += (temp // cost2) + 1
          i += 1
        
        return ways