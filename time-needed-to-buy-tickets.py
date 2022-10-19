class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0

        if tickets[k] == 0:
          return count
        else:
          while tickets[k] > 0:
            for i in range(len(tickets)):
              if tickets[i] != 0 and tickets[k] != 0:
                tickets[i] = tickets[i] - 1
                count = count + 1

        return count
      
        