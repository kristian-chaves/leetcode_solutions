class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.cap

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cap = val
        if(self.minStack):
            if(self.minStack[-1] >  val):
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if(self.stack):
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        return self.minStack[-1]


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