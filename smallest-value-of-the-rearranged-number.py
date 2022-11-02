class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            s = sorted(str(abs(num)))
            i = next(i for i,a in enumerate(s) if a > '0')
            s[i], s[0] = s[0], s[i]
            return int(''.join(s))
        else:
            s = sorted(str(abs(num)))
            return -int(''.join(s[::-1]))