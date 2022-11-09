class StockSpanner:

    def __init__(self):
        self.priceList = []
        
    def next(self, price: int) -> int:
        count = 1
        
        while self.priceList and self.priceList[-1][0] <= price:
            count += self.priceList.pop()[1]
        
        self.priceList.append([price, count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)