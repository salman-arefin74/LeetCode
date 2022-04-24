class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        indices = [i for i, x in enumerate(nums) if x == key]

        numKeyComparator = False
        kDistant = []
        for x in range(len(nums)):
            numKeyComparator = False
            for y in range(len(indices)):
                if abs(x - indices[y]) <= k:
                    numKeyComparator = True
            if numKeyComparator == True:
                kDistant.append(x)

        kDistant.sort()

        return kDistant