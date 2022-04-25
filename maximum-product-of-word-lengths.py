class Solution:
    def maxProduct(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                intersect = set(words[i]) & set(words[j])
                if(words[i] != words[j] and not intersect):
                    count = max(count, len(words[i]) * len(words[j]))      
        
        return count
