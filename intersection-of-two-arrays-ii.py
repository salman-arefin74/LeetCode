class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newNums = []

        for i in range(len(nums1)):
          for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
              newNums.append(nums2[j])
              nums2.pop(j)
              break
            
        return newNums