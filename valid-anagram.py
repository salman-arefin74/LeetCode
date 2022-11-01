from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t)
        
        for letter in freqS:
            if letter not in freqT:
                return False
            if freqS[letter] != freqT[letter]:
                return False
        for letter in freqT:
            if letter not in freqS:
                return False
        
        return True