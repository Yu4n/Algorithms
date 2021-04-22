class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = -int('inf')

    def push(self, val: int) -> None:
        if val < self.min_:
            self.min_ = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_ = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_
