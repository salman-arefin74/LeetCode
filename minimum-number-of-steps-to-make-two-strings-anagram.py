from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqS = Counter(s)
        freqT = Counter(t)
        steps = 0

        for letter in freqT:
          if letter in freqS:
            steps += abs(freqS[letter] - freqT[letter])
          else:
            steps += freqT[letter]

        for letter in freqS:
          if letter not in t:
            steps += freqS[letter]
        
        return steps // 2