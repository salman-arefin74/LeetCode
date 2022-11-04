class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot, equalToPivot, greaterThanPivot = [], [], []

        for item in nums:
            if item < pivot:
                lessThanPivot.append(item)
            elif item > pivot:
                greaterThanPivot.append(item)
            else:
                equalToPivot.append(item)
            
        return lessThanPivot + equalToPivot + greaterThanPivot