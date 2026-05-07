class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)
        if self.minstack==[] or val<=self.minstack[-1]:
            self.minstack.append(val)
        print(self.minstack,"min")

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack!=[]:
            return self.minstack[-1]
