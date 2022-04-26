class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for x in range(len(words)):
            if words[x].startswith(pref):
                count = count + 1
                
        return count
