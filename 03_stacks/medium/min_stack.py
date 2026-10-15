class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        # self.minstack.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        # least = float('inf')
        # for i in range(1,len(self.minstack)):
        #     least = min(least, self.minstack[i])
        # return least

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()