class MinStack:

    def __init__(self):
        self.stack = []
        #self.cap

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cap = val

    def pop(self) -> None:
        self.stack.pop()
        self.cap = self.stack[-1]

    def top(self) -> int:
        return self.cap

    def getMin(self) -> int:
        return self.stack.min()


# Your MinStack object will be instantiated and called as such:
#val = 4
#obj = MinStack()
#obj.push(val)
#obj.pop()
#param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2