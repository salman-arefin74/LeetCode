class Solution:
  def matrixReshape(self,nums, r, c):
    m = len(nums)
    n = len(nums[0])

    if (m*n) != (r*c):
      return nums

    result = [[0 for _ in range(c)] for _ in range(r)]
    
    k = 0
    for i in range(m):
      for j in range(n):
        result[k//c][k % c] = nums[i][j]
        k += 1

    return result