class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        
        for letter in range(len(s)):
            if result and s[letter] == result[-1]:
                result.pop()
            else:
                result.append(s[letter])
                        
        return ''.join(result)
