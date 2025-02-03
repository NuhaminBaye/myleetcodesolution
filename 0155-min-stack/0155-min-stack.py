class MinStack:
    def __init__(self):
        self.stk = []       # Main stack to hold values
        self.min_stk = []   # Stack to hold minimum values

    def push(self, val: int) -> None:
        self.stk.append(val)  # Push value onto the main stack
        # Push onto min_stk the minimum value so far
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        if self.stk:
            top_value = self.stk.pop()  # Pop from the main stack
            # If the popped value is the minimum, pop it from min_stk as well
            if top_value == self.min_stk[-1]:
                self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1] if self.stk else None  # Return the top element

    def getMin(self) -> int:
        return self.min_stk[-1] if self.min_stk else None  # Return the minimum element

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()