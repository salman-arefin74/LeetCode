class Solution(object):
    def countWords(self, words1, words2):
        words1dict = {words1[i] : words1.count(words1[i]) for i in range(len(words1))}
        words2dict = {words2[i] : words2.count(words2[i]) for i in range(len(words2))}

        words1list = []
        words2list = []

        for (x,y) in words1dict.items():
          if y == 1:
            words1list.append(x)

        for (x,y) in words2dict.items():
          if y == 1:
            words2list.append(x)

        count = 0
        for word in words1list:
          if word in words2list:
            count = count + 1
        
        return count
        