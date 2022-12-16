class MyQueue:

    def __init__(self):
        self.stack = list()
        self.top = 0
        self.ptr = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top+=1

    def pop(self) -> int:
        self.ptr+=1
        return self.stack[self.ptr-1]

    def peek(self) -> int:
        return self.stack[self.ptr]

    def empty(self) -> bool:
        return not self.top-self.ptr>0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()