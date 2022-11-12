class MedianFinder:

    def __init__(self):
        self.smallHeap, self.largeHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)

        if self.smallHeap and self.largeHeap and ((-1 * self.smallHeap[0]) > self.largeHeap[0]):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.smallHeap) > len(self.largeHeap):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.largeHeap) > len(self.smallHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)
            
    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        else:
            return ((-1 * self.smallHeap[0]) + self.largeHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
