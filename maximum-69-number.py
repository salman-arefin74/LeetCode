class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for n in range(len(s)):
            if s[n] == '6':
                s[n] = '9'
                break
        return int(''.join(s))
