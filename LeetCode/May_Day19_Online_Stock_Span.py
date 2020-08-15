class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack

        count = 1
        while stack and stack[-1][0] <= price:
            count += stack.pop()[1]
        stack.append((price, count))
        
        return count