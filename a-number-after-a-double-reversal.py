class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num1 = str(num)
        reverse1str = num1[::-1]
        reverse1 = int(reverse1str)

        num2 = str(reverse1)
        reverse2str = num2[::-1]
        reverse2 = int(reverse2str)
        
        if reverse2 == num:
            return True
        else:
            return False