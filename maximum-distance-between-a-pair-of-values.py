class Solution(object):
    def maxDistance(self, nums1, nums2):
        maxDistance = i = j = 0

        while i < len(nums1) and j < len(nums2):
          if nums1[i] > nums2[j]:
            i += 1
          else:
            maxDistance = max(maxDistance, j-i)
            j += 1
            
        return maxDistance
        