from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqS = Counter(s)
        freqT = Counter(t)
        steps = 0

        for letter in freqS:
          if letter in freqT:
            steps += abs(freqS[letter] - freqT[letter])
          else:
            steps += freqS[letter]

        for letter in freqT:
          if letter not in s:
            steps += freqT[letter]
            
        return steps