class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        summation = k * (k+1)/2
        summation = int(summation)
        visited = set()
        for x in nums:
            if x <= k and x not in visited:
                summation = summation - x
                summation = summation + k + 1
                k = k+1
                visited.add(x)

        return summation