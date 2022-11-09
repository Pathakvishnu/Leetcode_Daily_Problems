class StockSpanner:
    """
    If previous price in stack is more than stream input price than we just append it in stack 
    with span info in tuple for e.g. (price,span)

    If previous price is less than the stream input price than we pop previous price data and check next information
    until stack is empty or we encountered a condition where previous price is greater than input price.

    In 2nd step we will keep poping out the element and updating span data whenever we find previous price is less
    than input price.
    """

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        span = 0
        if not self.stack:
            self.stack.append((price,1)) # (price,span)
        else:
            while self.stack:
                prev_price,_ = self.stack[-1]
                if prev_price<=price:
                    prev_info = self.stack.pop()
                    span+=prev_info[1]
                else:
                    break
            
            self.stack.append((price,span+1))
        return span+1

# input 
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)