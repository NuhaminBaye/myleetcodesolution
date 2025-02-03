from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # Move all elements except the last one to the back of the deque
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        # The last element is the top of the stack, pop and return it
        return self.q.popleft()

    def top(self) -> int:
        # Move all elements except the last one to the back of the deque
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        # The last element is the top of the stack
        top_element = self.q.popleft()
        self.q.append(top_element)  # Put it back
        return top_element

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()